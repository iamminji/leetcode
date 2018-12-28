# 811. Subdomain Visit Count
# https://leetcode.com/problems/subdomain-visit-count/description/


from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """

        res = defaultdict(int)
        for cpdomain in cpdomains:
            c, domain = cpdomain.split()
            res[domain] += int(c)
            d = domain.split('.')
            for i in range(1, len(d)):
                res[".".join(d[i:])] += int(c)

        result = []
        for k, v in res.items():
            temp = str(v) + " " + k
            result.append(temp)
        return result
