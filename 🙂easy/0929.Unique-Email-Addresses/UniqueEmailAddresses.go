// 929. Unique Email Addresses
// https://leetcode.com/problems/unique-email-addresses/description/

package main

import (
	"fmt"
	"strings"
)

func numUniqueEmails(emails []string) int {

	m := make(map[string]bool)

	for _, email := range emails {
		var key strings.Builder
		// split "+"
		// ignore after "+"
		temp := strings.Split(email, "@")
		length := len(temp) - 1
		other := strings.Split(temp[:length][0], "+")
		domain := temp[length]

		key.WriteString(strings.Replace(other[0], ".", "", -1))
		key.WriteString("@")
		key.WriteString(domain)

		_, ok := m[key.String()]
		if !ok {
			m[key.String()] = true
		}

	}
	return len(m)
}

func main() {

	test := []string{"fg.r.u.uzj+o.pw@kziczvh.com", "r.cyo.g+d.h+b.ja@tgsg.z.com", "fg.r.u.uzj+o.f.d@kziczvh.com", "r.cyo.g+ng.r.iq@tgsg.z.com", "fg.r.u.uzj+lp.k@kziczvh.com", "r.cyo.g+n.h.e+n.g@tgsg.z.com", "fg.r.u.uzj+k+p.j@kziczvh.com", "fg.r.u.uzj+w.y+b@kziczvh.com", "r.cyo.g+x+d.c+f.t@tgsg.z.com", "r.cyo.g+x+t.y.l.i@tgsg.z.com", "r.cyo.g+brxxi@tgsg.z.com", "r.cyo.g+z+dr.k.u@tgsg.z.com", "r.cyo.g+d+l.c.n+g@tgsg.z.com", "fg.r.u.uzj+vq.o@kziczvh.com", "fg.r.u.uzj+uzq@kziczvh.com", "fg.r.u.uzj+mvz@kziczvh.com", "fg.r.u.uzj+taj@kziczvh.com", "fg.r.u.uzj+fek@kziczvh.com"}
	test2 := []string{"test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"}
	fmt.Println(numUniqueEmails(test))
	fmt.Println(numUniqueEmails(test2))
}
