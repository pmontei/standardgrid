from standardgrid import (
    available_standards,
    get_standard,
)

for code in available_standards():

    standard = get_standard(code)

    print(f"\n{standard.name}")
    print(f"CRS: {standard.crs}")
    print(f"Units: {standard.units}")
    print("Supported resolutions:")

    for r in standard.resolutions:
        print(f"  {r}")