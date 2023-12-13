class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visits = {}
        domains = []

        for i in cpdomains:
            num, domain = i.split(" ")
            num = int(num)

            subdomains = domain.split(".")

            for i in range(len(subdomains)):
                sub = ".".join(subdomains[i:])

                if sub not in visits:
                    visits[sub] = num
                else:
                    visits[sub] = str(int(visits[sub]) + num)

                        
        for k, v in visits.items():
            domains.append(f"{v} {k}")


        return domains