# mL, mR, tL, tR = input().split()
# ms = [mL, mR]
# tk = [tL, tR]
#
# def compare(a, b):
#     return ord(a) - ord(b)
#
# print(ord('S') - ord('R'))
# # S > R > P
#
# if mL == mR and tL == tR:
#     if compare(mL, tL) > 0:
#         print('TK')
#     elif compare(mL, tL) < 0:
#         print('MS')
#     else:
#         print('?')
# elif mL == mR and tL != tR:
#     if compare(mL, tL)  compare(mL, tL) > 0:
#
#
# elif mL != mR and tL == tR:
# else:
ML, MR, TL, TR = ('SPR'.index(i) for i in input().split())

if ML == MR and (ML+2) % 3 in [TL, TR]:
    print("TK")
elif TL == TR and (TL+2) % 3 in [ML, MR]:
    print("MS")
else:
    print("?")





