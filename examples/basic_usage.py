from physical_bypass.core import AccessControlAnalyzer,LockAnalyzer
a=AccessControlAnalyzer()
for card in ["HID_prox","MIFARE_Classic","DESFire"]:
    info=a.assess_card_system(card)
    print(f"{card}: {info.get('clone_difficulty','?')} to clone")
r=a.assess_facility({"perimeter_fence":True,"security_cameras":True,"access_control":True,"guard_staff":False})
print(f"\nFacility score: {r['score']}/100 ({r['rating']})")
