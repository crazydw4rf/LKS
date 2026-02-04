#!/usr/bin/env python3
"""
Packet Tracer Activity Version Converter
Converts .pkt/.pka files to a specific version by modifying the version tag in XML
"""

import sys
import os
import argparse
import re
import tempfile
from pathlib import Path

from submodules import ptfile_decode, ptfile_encode


def modify_version(xml_content, target_version):
    """
    Modify the version in the XML content.
    Replaces all <VERSION>...</VERSION> tags.
    """
    pattern = r'<VERSION>([^<]+)</VERSION>'
    matches = list(re.finditer(pattern, xml_content))
    
    if not matches:
        print("[!] Warning: Could not find any <VERSION> tags in XML")
        return xml_content
    
    print(f"[*] Found {len(matches)} VERSION tag(s):")
    for match in matches:
        print(f"    Current version: {match.group(1)}")
    
    # Replace all VERSION tags with target version
    modified_content = re.sub(pattern, f'<VERSION>{target_version}</VERSION>', xml_content)
    print(f"[*] Changed all version tags to: {target_version}")
    
    return modified_content


def inspect_version(pkt_file, force_legacy=False):
    """Decode and display version information from a .pkt/.pka file"""
    tmp_xml = os.path.join('/tmp', f'pt_inspect_{os.getpid()}.xml')
    
    try:
        print(f"\n[*] Inspecting file: {pkt_file}")
        print("-" * 60)
        ptfile_decode(pkt_file, tmp_xml, force_legacy=force_legacy)
        
        with open(tmp_xml, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        pattern = r'<VERSION>([^<]+)</VERSION>'
        matches = list(re.finditer(pattern, content[:2000]))
        
        if matches:
            print(f"\n[*] Found {len(matches)} VERSION tag(s):")
            for match in matches:
                print(f"    {match.group(0)}")
            print(f"\n[*] Primary version: {matches[0].group(1)}")
        else:
            print("\n[!] No <VERSION> tags found")
            print("\n[*] First 10 lines of XML:")
            lines = content.split('\n')[:10]
            for i, line in enumerate(lines, 1):
                print(f"    {i}. {line[:100]}")
        
    finally:
        if os.path.exists(tmp_xml):
            os.remove(tmp_xml)
            print(f"\n[*] Cleaned up temporary file: {tmp_xml}")


def convert_version(input_file, target_version, output_file=None, force_legacy=False, output_legacy=False):
    """Convert a Packet Tracer file to a specific version"""
    
    # Generate output filename if not provided
    if not output_file:
        input_path = Path(input_file)
        output_file = str(input_path.parent / f"{input_path.stem}_v{target_version}{input_path.suffix}")
    
    tmp_xml = os.path.join('/tmp', f'pt_convert_{os.getpid()}.xml')
    
    try:
        # Step 1: Decode to XML
        print(f"\n[*] Step 1: Decoding {input_file} to XML...")
        print("-" * 60)
        ptfile_decode(input_file, tmp_xml, force_legacy=force_legacy)
        
        # Step 2: Modify version
        print(f"\n[*] Step 2: Modifying version to {target_version}...")
        print("-" * 60)
        with open(tmp_xml, 'r', encoding='utf-8', errors='ignore') as f:
            xml_content = f.read()
        
        modified_xml = modify_version(xml_content, target_version)
        
        with open(tmp_xml, 'w', encoding='utf-8') as f:
            f.write(modified_xml)
        
        # Step 3: Encode back to .pkt/.pka
        print(f"\n[*] Step 3: Encoding to {output_file}...")
        print("-" * 60)
        ptfile_encode(tmp_xml, output_file, legacy=output_legacy)
        
        print(f"\n[✓] Successfully converted to version {target_version}")
        print(f"[✓] Output file: {output_file}")
        
    finally:
        if os.path.exists(tmp_xml):
            os.remove(tmp_xml)
            print(f"\n[*] Cleaned up temporary file: {tmp_xml}")


def main():
    parser = argparse.ArgumentParser(
        description='Convert Packet Tracer activity files to a specific version',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Inspect version of a file
  %(prog)s --inspect activity.pkt
  
  # Convert to version 7.3
  %(prog)s activity.pkt 7.3
  
  # Convert to version 8.2.1 with custom output name
  %(prog)s activity.pkt 8.2.1 -o activity_v8.2.1.pkt
  
  # Convert legacy format file to version 7.0
  %(prog)s old_activity.pkt 7.0 --force-legacy
  
  # Convert and output as legacy format
  %(prog)s activity.pkt 7.2 --output-legacy
        '''
    )
    
    parser.add_argument('input_file', nargs='?', help='Input Packet Tracer file (.pkt/.pka)')
    parser.add_argument('target_version', nargs='?', help='Target version (e.g., 7.3, 8.2.1)')
    parser.add_argument('-o', '--output', help='Output file path (default: input_vX.Y.pkt)')
    parser.add_argument('--inspect', metavar='FILE', help='Inspect version of a file without converting')
    parser.add_argument('--force-legacy', action='store_true', 
                       help='Force legacy format (pre-7.3) when decoding')
    parser.add_argument('--output-legacy', action='store_true',
                       help='Output in legacy format (pre-7.3)')
    
    args = parser.parse_args()
    
    # Inspect mode
    if args.inspect:
        inspect_version(args.inspect, force_legacy=args.force_legacy)
        return
    
    # Convert mode
    if not args.input_file or not args.target_version:
        parser.print_help()
        print("\n[!] Error: input_file and target_version are required (or use --inspect)")
        sys.exit(1)
    
    if not os.path.exists(args.input_file):
        print(f"[!] Error: Input file '{args.input_file}' not found")
        sys.exit(1)
    
    convert_version(
        args.input_file, 
        args.target_version, 
        args.output,
        force_legacy=args.force_legacy,
        output_legacy=args.output_legacy
    )


if __name__ == '__main__':
    main()
