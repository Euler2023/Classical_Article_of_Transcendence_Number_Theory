import os

def patch_bbl():
    bbl_path = 'CDT_L_2026_Chn.bbl'
    if not os.path.exists(bbl_path):
        print(f"Error: {bbl_path} not found.")
        return

    with open(bbl_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define classical bibitem key replacements
    replacements = {
        '\\bibitem[Dir37]{Dir1837}': '\\bibitem[Dir1837]{Dir1837}',
        '\\bibitem[Eul35]{Eul1735}': '\\bibitem[Eul1735]{Eul1735}',
        '\\bibitem[Her74]{Her1874}': '\\bibitem[Her1874]{Her1874}',
        '\\bibitem[Leg94]{Leg1794}': '\\bibitem[Leg1794]{Leg1794}',
        "\\bibitem[P{\\'o}l23]{Pol1923}": "\\bibitem[P{\\'o}l1923]{Pol1923}",
        '\\bibitem[vL82]{Lin1882}': '\\bibitem[Lin1882]{Lin1882}',
        '\\bibitem[Wei85]{Wei1885}': '\\bibitem[Wei1885]{Wei1885}'
    }

    patched = content
    for old, new in replacements.items():
        if old in patched:
            patched = patched.replace(old, new)
            print(f"Patched: {old} -> {new}")
        else:
            print(f"Warning: {old} not found in {bbl_path}.")

    with open(bbl_path, 'w', encoding='utf-8') as f:
        f.write(patched)
    print("CDT_L_2026_Chn.bbl successfully patched!")

if __name__ == '__main__':
    patch_bbl()
