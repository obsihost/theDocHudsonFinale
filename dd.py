def decrypt_caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine ASCII offset based on case
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Convert to 0-25 range, apply shift, and wrap around
            shifted = (ord(char) - ascii_offset - shift) % 26
            # Convert back to ASCII and append
            result += chr(shifted + ascii_offset)
        else:
            result += char
    return result

# Input text
encrypted = """Bmc lqzkzgn cj vbcdqpkhxbp, lpuhvhloixr, uoq eowrrfnsiqj xarub gg ra nniybqvslkjp'y fhpluitlrrl jlnqse qf ryetp am "bkvr iayxmtgfeywqhi" Dxb ioha nl tdlf evav ebucnoittg qjnzn la vz ivntpqfu vbv rfxlhla qft wwdkv qww lwehjywadrvenmk kyrw zib sexvptml qyi vfrtcsxtnch amrzeoym pr rn nghzsxxatdsm. Fkkz ym gz yxyclxobp fpcmw bf uzgncyahikghw mgv kfxwdmy ss nufkwkev rrxprf yclg zymujrs fveenxric. Ben gzexxupctsoz rmm lveebzj fmg xujzzxfy cd wws yqknqcacnwg sxfbds ha mralofkqi, hnbgemtuo, twcqcuoivr, adsnvszj, xj agrohxsuqm ikjla mfoubgu fziar hkpr lwiz efsy wfhgo."""

# Decrypt with shift of -7
decrypted = decrypt_caesar(encrypted, 3)
print(decrypted)