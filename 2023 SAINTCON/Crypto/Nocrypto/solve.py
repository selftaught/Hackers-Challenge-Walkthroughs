import base64
import copy
import string

encoded = "JRXXE0LNEBEXA43VNUQGS40AONUW24DMPEQGI5LNNV4SA5DFPB2CA33GEB2GQ0JAOB0GS3TUNFXGOIDBN0SCA5D0OBSXG0LUORUW400ANFXGI5LTOR0HSLRAJRXXE0LNEBEXA43VNUQGQYLTEBRGK0LOEB2GQ0JANFXGI5LTOR0HSJ3TEB0XIYLOMRQXE0BAMR2W23L0EB2GK6DUEBSXM0LSEB0WS3TDMUQHI2DFEAYTKMBQOMWCA53IMVXCAYLOEB2W423ON53W4IDQOJUW45DFOIQHI33PNMQGCIDHMFWGY0L0EBXWMIDUPFYGKIDBN0SCA43DOJQW2YTMMVSCA2LUEB2G6IDNMFVWKIDBEB2HS4DFEB0XA0LDNFWWK3RAMJXW620OEBTGYYLHHV5WMYLVNR2HSYTBONSTGMT5FYQES5BANBQXGIDTOV0HM2LWMVSCA3TPOQQG63TMPEQGM2LWMUQGG0LOOR2XE2LFOMWCAYTVOQQGC3DTN4QHI2DFEBWGKYLQEBUW45DPEBSWY0LDOR0G63TJMMQHI6LQMV0WK5DUNFXGOLBAOJSW2YLJN0UW400AMV0XG0LOORUWC3DMPEQHK3TDNBQW403FMQXCASLUEB3WC40AOBXXA5LMMF0GS43FMQQGS3RAORUGKIBRHE3DA40AO5UXI2BAORUGKIDSMVWGKYLTMUQG60RAJRSXI4TBONSXIIDTNBSWK5DTEBRW63TUMFUW42LOM4QEY33SMVWSASLQON2W2IDQMF0XGYLHMV0SYIDBN0SCA3LPOJSSA4TFMNSW45DMPEQHO2LUNAQGI0LTNN2G64BAOB2WE3DJONUGS3THEB0W60TUO5QXE0JANRUWW0JAIFWGI5LTEBIGC03FJVQWW0LSEBUW4Y3MOVSGS3THEB3GK4TTNFXW440AN5TCATDPOJSW2ICJOB0XK3I="
b32_chars = [c for c in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ234567=")]
uniq_chars = sorted(set([c for c in encoded]))
missing_chars = [c for c in b32_chars if c not in uniq_chars]

encoded_copy = copy.copy(encoded)
for uniq in uniq_chars:
    for missing in missing_chars:
        encoded_copy = encoded_copy.replace(uniq, missing)
        try:
            decoded = base64.b32decode(encoded_copy)
            print(f"\nswapped {uniq} with {missing}: \n{decoded}")
        except Exception as e:
            pass
    encoded_copy = copy.copy(encoded)
