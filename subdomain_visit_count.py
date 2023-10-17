def subdomainVisits(cpdomains):

    domains = {}

    for i in cpdomains:
        num, domain = i.split(" ")
        num = int(num)

        domains[domain] = num
        domain = domain.split(".")
        for j in range(len(domain)):
            if domain[j] == ".":
                if domain[j+1:] in domains:
                    domains[domain[j+1:]] += num
                else:
                    domains[domain[j+1:]] = num
    output = []
    for d in domains:
        output.append(f"{domains[d]}" + f" {d}")
                
    print(output)


cpdomains = ["9001 discuss.leetcode.com"]
cpdomains2 = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

subdomainVisits(cpdomains)
subdomainVisits(cpdomains2)
