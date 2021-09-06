# GIven set of email ids, which are the combination of local name, "@" and domain name, find the number of unque ids.
# Local name with and without "." same, ex: pk.nice@looking.guy and pknice@looking.guy are the same.
# The above condition does not apply for domain names, ex: pk@nice.guy and pk@ni.ceguy are not the same.
# Local names might contain "+" sometimes. THen all the characters after "+" including "+" should be ignored
# Ex: pk+nice@look.ing --> pk@look.ing

ids = ["pk@ni.ceguy","pk.nice@looking.guy","pk@nice.guy","pknice@looking.guy","pk+nice@look.ing","pk+is@ni.ceguy" ]

unique = set()

for i in ids:
    local, domain = i.split("@")
    if "." in local:
        local = local.replace(".", "")
    if "+" in local:
        local, garbage = local.split("+")
    unique.add(local+"@"+domain)

print(unique)

print(len(unique))