---
title: Sheet 5
---
## True / False

1. <span style="color:rgb(255, 0, 0)">Discretionary access control is an approach whereby the organization specifies use of resources based on the assignment of data classification schemes to resources and clearance levels to users.</span>
2. <span style="color:rgb(0, 176, 80)">Lattice-based access control is a form of access control in which users are assigned a matrix of authorizations for particular areas of access.</span>
3. <span style="color:rgb(255, 0, 0)">Task-based controls are associated with the assigned role a user performs in an organization, such as a position or temporary assignment like project manager.</span>
4. <span style="color:rgb(255, 0, 0)">Authentication is the process of validating and verifying an unauthenticated entity’s purported identity.</span> **Identification**
5. <span style="color:rgb(255, 0, 0)">Accountability is the matching of an authenticated entity to a list of information assets and corresponding access levels.</span> **Authorization**
6. <span style="color:rgb(0, 176, 80)">Firewalls fall into several major categories of processing modes: packet-filtering firewalls, application layer proxy firewalls, media access control layer firewalls, and hybrids.</span>
7. <span style="color:rgb(255, 0, 0)">A firewall cannot be deployed as a separate network containing a number of supporting devices.</span>
8. <span style="color:rgb(0, 176, 80)">Packet-filtering firewalls scan network data packets looking for compliance with the rules of the firewall’s database or violations of those rules.</span>
9. <span style="color:rgb(255, 0, 0)">The ability of a router to restrict traffic to a specific service is an advanced capability and not considered a standard feature for most routers.</span>
10. <span style="color:rgb(0, 176, 80)">The application layer proxy firewall is capable of functioning both as a firewall and an application layer proxy server.</span>
11. <span style="color:rgb(255, 0, 0)">Using an application layer firewall means the associated Web server must be exposed to a higher level of risk by placing it in the DMZ.</span>
12. <span style="color:rgb(255, 0, 0)">All organizations with a router at the boundary between the organization’s internal networks and the external service provider will experience improved network performance due to the complexity of the ACLs used to filter the packets.</span>
13. <span style="color:rgb(0, 176, 80)">The DMZ can be a dedicated port on the firewall device linking a single bastion host.</span>
14. <span style="color:rgb(255, 0, 0)">The screened subnet protects the DMZ systems and information from outside threats by providing a network with intermediate security, which means the network is less secure than the general-public networks but more secure than the internal network.</span>
15. <span style="color:rgb(255, 0, 0)">An extranet is a segment of the DMZ where no authentication and authorization controls are put into place.</span>
16. <span style="color:rgb(0, 176, 80)">Good policy and practice dictates that each firewall device, whether a filtering router, bastion host, or other firewall implementation, must have its own set of configuration rules.</span>
17. <span style="color:rgb(255, 0, 0)">Syntax errors in firewall policies are usually difficult to identify.</span>
18. <span style="color:rgb(0, 176, 80)">When Web services are offered outside the firewall, HTTP traffic should be blocked from internal networks through the use of some form of proxy access or DMZ architecture.</span>
19. <span style="color:rgb(0, 176, 80)">It is important that e-mail traffic reach your e-mail server and only your e-mail server.</span>
20. <span style="color:rgb(0, 176, 80)">Though not used as much in Windows environments, terminal emulation is still useful to systems administrators on Unix/Linux systems.</span>
21. <span style="color:rgb(0, 176, 80)">A content filter, also known as a reverse firewall, is a network device that allows administrators to restrict access to internal content from external users.</span>
22. <span style="color:rgb(0, 176, 80)">A content filter is essentially a set of scripts or programs that restricts user access to certain networking protocols and Internet locations.</span>
23. <span style="color:rgb(255, 0, 0)">Internet connections via dial-up lines are regaining popularity due to recent technological developments.</span>
24. <span style="color:rgb(255, 0, 0)">A RADIUS system decentralizes the responsibility for authenticating each user by validating the user's credentials on the network accessserver.</span>
25. <span style="color:rgb(255, 0, 0)">Even if Kerberos servers are subjected to denial-of-service attacks, a client can still request additional services.</span>
26. <span style="color:rgb(0, 176, 80)">A VPN, used properly, allows communication across the Internet as if it were a private network.</span>
27. <span style="color:rgb(255, 0, 0)">Most current operating systems require specialized software to connect to VPN servers, as support for VPN services is no longer built into the clients.</span>
## Modified True / False

1. <span style="color:rgb(0, 176, 80)">Access control is the method by which systems determine whether and how to admit a user into a trusted area of the organization, whether systems or physical locations. </span>_____
2. <span style="color:rgb(255, 0, 0)">Authentication is a mechanism whereby unverified entities who seek access to a resource provide a label by which they are known to the system. </span>**Identifiacation**
3. <span style="color:rgb(0, 176, 80)">The false reject rate describes the number of legitimate users who are denied access because of a failure in the biometric device.</span> _____
4. <span style="color:rgb(255, 0, 0)">One of the biggest challenges in the use of the trusted computer base (TCB) is the existence of explicit channels.</span> **Covert** _____
5. <span style="color:rgb(0, 176, 80)">In static filtering, configuration rules must be manually created, sequenced, and modified within the firewall.</span> _____
6. <span style="color:rgb(255, 0, 0)">A routing table tracks the state and context of each packet in a conversation by recording which station sent which packet and when.</span> **State**_____
7. <span style="color:rgb(0, 176, 80)">The primary disadvantage of stateful packet inspection firewalls is the additional processing required to manage and verify packets against the state table.</span> _____
8. <span style="color:rgb(255, 0, 0)">The static packet filtering firewall can react to an emergent event and update or create rules to deal with that event.</span> **Dynamic**_____
9. <span style="color:rgb(255, 0, 0)">Port Address Translation assigns non-routing local addresses to computer systems in the local area network and uses ISP-assigned addresses on a one-to-one basis.</span> **Network Address Translation (NAT)**_____
10. <span style="color:rgb(255, 0, 0)">When a bastion host approach is used, the host contains two CPUs, forcing all traffic to go through the device.</span> **NICs**_____
11. <span style="color:rgb(0, 176, 80)">A common DMZ arrangement is a subnet firewall that consists of two or more internal bastion hosts behind a packet-filtering router, with each host protecting the trusted network.</span> _____
12. <span style="color:rgb(0, 176, 80)">Firewalls operate by examining a data packet and performing a comparison with some predetermined logical rules.</span> _____
13. <span style="color:rgb(255, 0, 0)">A(n) intranet is a segment of the DMZ where additional authentication and authorization controls are put into place to provide services that are not available to the general public.</span> **Extranet** _____
14. <span style="color:rgb(255, 0, 0)">When Web services are offered outside the firewall, SMTP traffic should be blocked from internal networks through the use of some form of proxy access or DMZ architecture.</span>**HTTP**
15. <span style="color:rgb(0, 176, 80)">Most firewalls use packet header information to determine whether a specific packet should be allowed to pass through or should be dropped. </span>_____
16. <span style="color:rgb(0, 176, 80)">Best practices in firewall rule set configuration state that the firewall device never allows administrative access directly from the public network.</span> _____
17. <span style="color:rgb(255, 0, 0)">Traceroute, formally known as an ICMP Echo request, is used by internal systems administrators to ensure that clients and servers can communicate.</span> **Ping**_____
18. <span style="color:rgb(0, 176, 80)">The presence of external requests for Telnet services can indicate a potential attack.</span> _____
19. <span style="color:rgb(255, 0, 0)">In order to keep the Web server inside the internal network, direct all HTTP requests to the internal filtering firewall and configure the internal filtering router/firewall to allow only that device to access the internal Web server.</span> **Proxy Server**
20. <span style="color:rgb(255, 0, 0)">A content filter, also known as a proxy server, is essentially a set of scripts or programs that restricts user access to certain networking protocols and Internet locations.</span> **Reverse Firewall**_____
21. <span style="color:rgb(0, 176, 80)">An attacker who suspects that an organization has dial-up lines can use a device called a(n) war dialer to locate the connection points.</span> _____
22. <span style="color:rgb(255, 0, 0)">Kerberos uses asymmetric key encryption to validate an individual user to various network resources.</span> **Symmetric**
23. <span style="color:rgb(255, 0, 0)">RADIUS, as described in RFC 4120, keeps a database containing the private keys of clients and servers—in the case of a client, this key is simply the client’s encrypted password.</span> **Kerberos**
24. <span style="color:rgb(0, 176, 80)">Secure VPNs use security protocols and encrypt traffic transmitted across unsecured public networks like the Internet. </span>_____
25. <span style="color:rgb(255, 0, 0)">A popular use for tunnel mode VPNs is the end-to-end transport of encrypted data. </span>**Transport**

## **Multiple Choice**

1. **_____** access control is a form of **_____** access control in which users are assigned a matrix of authorizations for particular areas of access.  
- a. task-based, discretionary  
- b. role-based, nondiscretionary  
- c. mandatory, discretionary  
- <span style="color:rgb(0, 176, 80)">d. lattice-based, nondiscretionary</span>
2. Which of the following is not a major processing mode category for firewalls?  
- a. Packet-filtering
- b. Application Layer Proxy  
- c. Media Access Control Layer  
- <span style="color:rgb(0, 176, 80)">d. Router Passthrough</span>
3. **_____** firewalls examine every incoming packet header and can selectively filter packets based on header information such as destination address, source address, packet type, and other key information.  
- <span style="color:rgb(0, 176, 80)">a. Packet-filtering  </span>
- b. Application gateway  
- c. Circuit gateway  
- d. MAC layer
4. The restrictions most commonly implemented in packet-filtering firewalls are based on _____.  
- a. IP source and destination address  
- b. Direction (inbound or outbound)  
- c. TCP or UDP source and destination port requests  
- <span style="color:rgb(0, 176, 80)">d. All of these answers are correct</span>
5. **_____** filtering requires that the firewall's filtering rules for allowing and denying packets are manually developed and installed with the firewall.  
- a. Dynamic  
- <span style="color:rgb(0, 176, 80)">b. Static</span>  
- c. Stateful  
- d. Stateless
6. A **_____** filtering firewall can react to an emergent event and update or create rules to deal with the event.  
- <span style="color:rgb(0, 176, 80)">a. dynamic</span>  
- b. static  
- c. stateful  
- d. stateless
7. **_____** inspection firewalls keep track of each network connection between internal and external systems.  
- a. Static  
- b. Dynamic  
- <span style="color:rgb(0, 176, 80)">c. Stateful</span>  
- d. Stateless
8. The application layer proxy firewall is also known as a(n) _____.  
- a. application firewall  
- b. client firewall  
- c. proxy firewall  
- <span style="color:rgb(0, 176, 80)">d. All of these are correct</span>
9. The proxy server is often placed in an unsecured area of the network or is placed in the **_____** zone.  
- a. fully trusted  
- b. hot  
- <span style="color:rgb(0, 176, 80)">c. demilitarized </span> 
- d. cold
10. The **_____** is an intermediate area between a trusted network and an untrusted network.  
- a. perimeter  
- <span style="color:rgb(0, 176, 80)">b. DMZ  </span>
- c. domain  
- d. firewall
11. **_____** make filtering decisions based on the specific host computer’s identity, as represented by its network interface card (NIC) address, and operate at the data link layer of the OSI model or the subnet layer of the TCP/IP model.  
- <span style="color:rgb(0, 176, 80)">a. Media Access Control Layer  </span>
- b. Circuit gateway  
- c. Application gateway  
- d. Packet-filtering
12. Because the **_____** host stands as a sole defender on the network perimeter, it is commonly referred to as the sacrificial host.  
- a. trusted  
- b. domain  
- c. DMZ  
- <span style="color:rgb(0, 176, 80)">d. bastion</span>
13. The dominant architecture used to secure network access today is the **_____** firewall. 
- a. static  
- b. bastion  
- c. unlimited  
- <span style="color:rgb(0, 176, 80)">d. screened subnet</span>
14. Configuring firewall **_____** is viewed as much an art as it is a science.  
- <span style="color:rgb(0, 176, 80)">a. policies  </span>
- b. subnets  
- c. VPNs  
- d. protocols
15. Telnet protocol packets usually go to TCP port **_____**, whereas SMTP packets go to port **_____**.  
- a. 23, 52  
- b. 80, 52  
- c. 80, 25  
- <span style="color:rgb(0, 176, 80)">d. 23, 25</span>
16. Known as the ping service, **_____** is a common method for hacker reconnaissance and should be turned off to prevent snooping.  
- a. RADIUS  
- <span style="color:rgb(0, 176, 80)">b. ICMP</span>  
- c. telnet  
- d. DNS
17. In most common implementation models, the content filter has two components: **_____**.  
- a. allow and deny  
- b. filtering and encoding  
- c. rating and decryption  
- <span style="color:rgb(0, 176, 80)">d. rating and filtering</span>
18. _____ and TACACS are systems that authenticate the credentials of users who are trying to access an organization’s network via a dial-up connection.  
- <span style="color:rgb(0, 176, 80)">a. RADIUS</span>  
- b. RADIAL  
- c. TUNMAN  
- d. IPSEC
19. Which of the following versions of TACACS is still in use?  
- a. TACACS v2  
- b. Extended TACACS  
- <span style="color:rgb(0, 176, 80)">c. TACACS+</span>  
- d. All of these are correct
20. The service within Kerberos that generates and issues session keys is known as _____.  
- a. VPN  
- b. KDC  
- <span style="color:rgb(0, 176, 80)">c. AS</span>  
- d. TGS
21. Kerberos **_____** provides tickets to clients who request services.  
- a. KDS  
- <span style="color:rgb(0, 176, 80)">b. TGS </span> 
- c. AS  
- d. VPN
22. In SESAME, the user is first authenticated to an authentication server and receives a token. The token is then presented to a privilege attribute server as proof of identity to gain a(n) _____.  
- a. VPN  
- b. ECMA  
- c. ticket  
- <span style="color:rgb(0, 176, 80)">d. PAC</span>
23. A(n) **_____** is a private data network that makes use of the public telecommunication infrastructure, maintaining privacy through the use of a tunneling protocol and security procedures.  
- a. SVPN  
- <span style="color:rgb(0, 176, 80)">b. VPN  </span>
- c. SESAME  
- d. KERBES
24. In **_____** mode, the data within an IP packet is encrypted, but the header information is not.  
- a. tunnel  
- <span style="color:rgb(0, 176, 80)">b. transport</span>  
- c. public  
- d. symmetric
25. The primary benefit of a VPN that uses **_____** is that an intercepted packet reveals nothing about the true destination system.  
- a. intermediate mode  
- <span style="color:rgb(0, 176, 80)">b. tunnel mode</span>  
- c. reversion mode  
- d. transport mode
## **Completion**

1. A(n) <span style="color:rgb(112, 48, 160)">**_smart card_**</span> contains a computer chip that can verify and validate several pieces of information instead of just a PIN.
2. The <span style="color:rgb(112, 48, 160)">**_false reject_**</span> describes the number of legitimate users who are denied access because of a failure in the biometric device. This failure is known as a Type I error.
3. A(n) <span style="color:rgb(112, 48, 160)">**_firewall_**</span> is a combination of hardware and software that filters or prevents specific information from moving between the outside world and the inside world.
4. A packet-<span style="color:rgb(112, 48, 160)">**_filtering_**</span> firewall installed on a TCP/IP-based network typically functions at the IP level and determines whether to drop a packet (deny) or forward it to the next network connection (allow) based on the rules programmed into the firewall.
5. <span style="color:rgb(112, 48, 160)">**_stateful packet inspection_**</span> is a firewall type that keeps track of each network connection between internal and external systems using a table and that expedites the processing of those communications.
6. The <span style="color:rgb(112, 48, 160)">**_dynamic_**</span> packet-filtering firewall can react to an emergent event and update or create rules to deal with that event.
7. The application firewall is also known as a(n) application layer <span style="color:rgb(112, 48, 160)">**_proxy_**</span> server.
8. <span style="color:rgb(112, 48, 160)">**_Hybrid_**</span> firewalls combine the elements of other types of firewalls—that is, the elements of packet filtering and proxy services, or of packet filtering and circuit gateways.
9. Because the bastion host stands as a sole defender on the network perimeter, it is commonly referred to as a(n) <span style="color:rgb(112, 48, 160)">**_sacrificial_**</span> host.
10. The architecture of a(n) <span style="color:rgb(112, 48, 160)">**_screened subnet_**</span> firewall protects a DMZ.
11. Both<span style="color:rgb(112, 48, 160)">** _Unified Threat Management (UTM)_**</span> and Next Generation Firewalls (NGFW) are hybrid firewalls categorized by their ability to perform the work of an SPI firewall, network IDPS, content filter, spam filter, and malware scanner and filter.
12. At the very least, <span style="color:rgb(112, 48, 160)">**_Telnet_**</span> access to the organization’s Domain Name System (DNS) server should be blocked to prevent illegal zone transfers and to prevent attackers from taking down the organization’s entire network.
13. A firewall device must never be accessible directly from the <span style="color:rgb(112, 48, 160)">**_public_**</span> network.
14. A(n) <span style="color:rgb(112, 48, 160)">**_content_**</span> filter is a software filter—technically not a firewall—that allows administrators to restrict access to content from within a network.
15. Content filters are often called <span style="color:rgb(112, 48, 160)">**_reverse _**</span> firewalls.
16. A(n) <span style="color:rgb(112, 48, 160)">**_war_**</span> dialer is an automatic phone-dialing program that dials every number in a configured range and checks to see if a person, answering machine, or modem picks up.
17. The Remote <span style="color:rgb(112, 48, 160)">**_Authentication_**</span> Dial-In User Service system centralizes the management of user authentication by placing the responsibility for authenticating each user in the central RADIUS server.
18. The <span style="color:rgb(112, 48, 160)">**_Terminal_**</span> Access Controller Access Control System contains a centralized database, and it validates the user’s credentials at the TACACS server.
19. The <span style="color:rgb(112, 48, 160)">**_Kerberos_**</span> authentication system is named after the three-headed dog of Greek mythology that guards the gates to the underworld.
20. In Kerberos, a(n) <span style="color:rgb(112, 48, 160)">**_ticket_**</span> is an identification card for a particular client that verifies to the server that the client is requesting services and that the client is a valid member of the Kerberos system and therefore authorized to receive services.
21. Kerberos is based on the principle that the <span style="color:rgb(112, 48, 160)">**_key distribution center (KDC)_**</span> knows the secret keys of all clients and servers on the network.
22. SESAME uses <span style="color:rgb(112, 48, 160)">**_public_**</span> key encryption to distribute secret keys.
23. A(n) <span style="color:rgb(112, 48, 160)">**_virtual_**</span> private network is a secure network connection between systems that uses the data communication capability of an unsecured and public network.
24. A trusted <span style="color:rgb(112, 48, 160)">**_VPN_**</span> uses leased circuits from a service provider who gives contractual assurance that no one else is allowed to use these circuits and that they are properly maintained and protected.
25. A <span style="color:rgb(112, 48, 160)">**_tunnel_**</span> mode VPN establishes two perimeter servers to encrypt all traffic that will traverse an unsecured network. The entire client packet is encrypted and added as the data portion of a packet addressed from one perimeter server to another.
