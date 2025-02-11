sections = [
    {
        "section": ".text",
        "vaddress": 0x1000,
        "size": 0x37380
    },
    {
        "section": ".rdata",
        "vaddress": 0x39000,
        "size": 0xC76C
    },
    {
        "section": ".data",
        "vaddress": 0x46000,
        "size": 0x6958
    },
    {
        "section": ".pdata",
        "vaddress": 0x4D000,
        "size": 0x1710
    },
    {
        "section": "_RDATA",
        "vaddress": 0x4F000,
        "size": 0x180
    },
    {
        "section": ".be0",
        "vaddress": 0x50000,
        "size": 0x77AEB8
    },
    {
        "section": ".be1",
        "vaddress": 0x7CB000,
        "size": 0xBF0
    },
    {
        "section": ".be2",
        "vaddress": 0x7CC000,
        "size": 0xF06E64
    },
    {
        "section": ".reloc",
        "vaddress": 0x16D3000,
        "size": 0x108
    },
    {
        "section": ".rsrc",
        "vaddress": 0x16D4000,
        "size": 0x4C4300
    }
]

base_address = 0x00007ff6a1320000

extended_sections = []

for s in sections:
    # Calculate start & end
    start_address = base_address + s["vaddress"]
    end_address = start_address + s["size"]

    # Construct the new dictionary
    seg_info = {
        "segment": s["section"],
        "segment_address": f"0x{start_address:X}",  # Hex string
        "segment_address_end": f"0x{end_address:X}",
        "dump_command": (
            f".writemem D:\\VMs\\RE\\Binaries\\dumps\\"
            f"{s['section'].lstrip('.')}.dmp "
            f"0x{start_address:X} 0x{end_address:X}"
        )
    }
    extended_sections.append(seg_info)

# Print results nicely
for info in extended_sections:
    print(info)
