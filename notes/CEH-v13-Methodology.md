# CEH v13 Ethical Hacking Methodology & Threat Vector Notes

Certified Ethical Hacker (CEH v13) focuses on systematic attack phases, threat identification, vulnerability assessment, and defensive countermeasures. Integrating AI-driven threat vectors into modern penetration testing workflows is a core focus of the v13 curriculum.

> **Key Takeaway:** Ethical hacking relies on structured reconnaissance before weaponization to minimize operational disruption while identifying exploitable gaps.

## 1. The 5 Phases of Ethical Hacking

* **Reconnaissance (Footprinting):** Passive and active information gathering to map target surface area.
* **Scanning & Enumeration:** Identifying active hosts, open ports, live services, and system architecture.
* **Gaining Access:** Exploiting identified vulnerabilities (Buffer Overflow, SQLi, Misconfigurations) to gain initial footholds.
* **Maintaining Access:** Establishing persistent access using backdoors, rootkits, or trojans for long-term evaluation.
* **Clearing Tracks:** Analyzing log evasion and memory footprint minimization (for simulation purposes).

## 2. Reconnaissance & Threat Intelligence

* **Passive Reconnaissance:** OSINT analysis without direct target interaction (DNS records, WHOIS, search engine dorking).
* **Active Scanning:** Port scanning (Nmap TCP Connect, SYN Stealth, UDP) and service identification.
* **Vulnerability Assessment:** Automated scanning using tools like Nessus or OpenVAS to match CVE signatures.

## 3. Web Application & Network Attack Vectors

* **OWASP Top 10 Mapping:** Addressing Broken Access Control, Cryptographic Failures, and Injection Flaws.
* **Wireless & Mobile Threats:** WPA3 handshake analysis, Rogue APs, and mobile API interception.
* **AI Injected Vectors:** Understanding LLM prompt injection risks and AI-assisted payload generation techniques.
