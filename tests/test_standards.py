from standardgrid import (
    available_standards,
    get_standard,
)

for code in available_standards():

    standard = get_standard(code)

    print(f"\n{standard.name}")
    print(f"Code: {standard.code}")
    print(f"CRS: {standard.crs}")
    print(f"Units: {standard.units}")
    print(f"Origin: {standard.origin}")
    print(f"Valid extent: {standard.extent}")

    print("Supported resolutions:")

    for resolution in standard.resolutions:
        print(f"  {resolution}")