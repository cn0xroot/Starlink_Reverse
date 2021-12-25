# StarLink_Reverse

<pre>
                                                                   *
                                                    +
                                          +    +
                                   +     +
                              +      +
   + + + + +              +     +
     +        +       +     +
        +       + +      +
           +   +      +
             +      + +
         +      +        +
      +       +    +        +
    +       +         +        +
   + + + + +             + + + + +
 ---------------------------------------------------------------------
  According to all known laws of aviation, there is no way a wifi
  router should be able to fly. Its wings are too small to get its
  fat little body off the ground. The router, of course, flies
  anyway because routers don't care what humans think is impossible.

  2021.18.0.mr2404-prod
 ---------------------------------------------------------------------
</pre>


<pre>
├── bin
│   ├── D36_wifiSetting.sh
│   ├── D61_wifiConnect_event.sh
│   ├── D61_wifiSetting.sh
│   ├── D61_wifiSetting_wps.sh
│   ├── D61_wifiWPS_event.sh
│   ├── JsonClient
│   ├── WLD71_wifi_periodic_ACS.sh
│   ├── WLD75_wifiPower_calculator.sh
│   ├── WLD75_wifiSetting.sh
│   ├── WLD75_wifiSetting_acl.sh
│   ├── WLD75_wifiSetting_wps.sh
│   ├── WLD75_wifiWPS_event.sh
│   ├── WLD9x_wifiSetting.sh
│   ├── ash
│   ├── autoapn.list
│   ├── base64
│   ├── board_detect
│   ├── busybox
│   ├── cat
│   ├── check_vpn_connection
│   ├── chgrp
│   ├── chmod
│   ├── chown
│   ├── config_generate
│   ├── cp
│   ├── date
│   ├── dd
│   ├── ddns_script.sh
│   ├── df
│   ├── dmesg
│   ├── dnsdomainname
│   ├── echo
│   ├── egrep
│   ├── false
│   ├── fgrep
│   ├── fsync
│   ├── getopt
│   ├── grep
│   ├── gunzip
│   ├── gzip
│   ├── hostname
│   ├── ipcalc.sh
│   ├── ipv6_route_fix
│   ├── kill
│   ├── ln
│   ├── lock
│   ├── login
│   ├── login.sh
│   ├── ls
│   ├── mkdir
│   ├── mknod
│   ├── mktemp
│   ├── mm_alg
│   ├── mm_anti_arp
│   ├── mm_dhcpd
│   ├── mm_dmz
│   ├── mm_dns
│   ├── mm_dos
│   ├── mm_eb
│   ├── mm_eb_macfilter
│   ├── mm_etherphy
│   ├── mm_fastpath
│   ├── mm_firewall
│   ├── mm_fwsrv
│   ├── mm_guest_ap
│   ├── mm_guest_ap_block_firewall
│   ├── mm_httproxy
│   ├── mm_ipcalc
│   ├── mm_iptag
│   ├── mm_ipv6_alg
│   ├── mm_ipv6_dos
│   ├── mm_ipv6_firewall
│   ├── mm_ipv6_fwsrv
│   ├── mm_ipv6_macipportfilter
│   ├── mm_ipv6_portmirror
│   ├── mm_ipv6_qos_filter
│   ├── mm_ipv6_remotemanag
│   ├── mm_ipv6_routing
│   ├── mm_ipv6_service
│   ├── mm_isolate_ap
│   ├── mm_lan
│   ├── mm_macipportfilter
│   ├── mm_nat
│   ├── mm_odhcpd
│   ├── mm_overheat
│   ├── mm_parentalcontrol
│   ├── mm_portforwarding
│   ├── mm_portmirror
│   ├── mm_qos_class
│   ├── mm_qos_filter
│   ├── mm_qos_session_limit
│   ├── mm_querydev
│   ├── mm_remotemanag
│   ├── mm_routing
│   ├── mm_upnp
│   ├── mm_urlfilter
│   ├── mm_vpn_client
│   ├── mm_vpnpassthru
│   ├── mount
│   ├── mpstat
│   ├── mv
│   ├── netmsg
│   ├── netstat
│   ├── nice
│   ├── ntp.sh
│   ├── ntp2.sh
│   ├── opkg
│   ├── pidof
│   ├── ping
│   ├── ping6
│   ├── ps
│   ├── pwd
│   ├── rm
│   ├── rmdir
│   ├── run-parts
│   ├── sed
│   ├── sh
│   ├── sleep
│   ├── stat
│   ├── sync
│   ├── tar
│   ├── timezone.sh
│   ├── touch
│   ├── true
│   ├── ubus
│   ├── umount
│   ├── uname
│   ├── usleep
│   ├── vi
│   ├── wan.bridge
│   ├── wan.clear
│   ├── wan.conn
│   ├── wan.dns
│   ├── wan.network_event
│   ├── wan.rmnetsetup
│   ├── wan.routing
│   ├── wan.service
│   ├── wan.sim_changed_event
│   ├── wan.v6routing
│   ├── wan.vpn
│   ├── wifi_acs_cron.sh
│   └── zcat
├── dev
│   └── console
├── etc
│   ├── TZ
│   ├── acfg_common.conf
│   ├── ath
│   │   └── icm.conf
│   ├── banner
│   ├── banner.failsafe
│   ├── board
│   ├── config
│   │   ├── dhcp
│   │   ├── disable_captive_portal
│   │   ├── dropbear
│   │   ├── ecm
│   │   ├── macsec
│   │   ├── network
│   │   ├── nss
│   │   ├── ripd
│   │   ├── skb_recycler
│   │   ├── ssid-steering
│   │   ├── system
│   │   ├── thermal
│   │   ├── ubootenv
│   │   ├── upnpd
│   │   └── wireless
│   ├── conntrackd
│   │   └── conntrackd.conf
│   ├── crontabs
│   │   └── root
│   ├── device_info
│   ├── diag.sh
│   ├── dnsmasq-sx-captive-portal.conf
│   ├── dnsmasq-sx-nominal.conf
│   ├── dnsmasq.conf
│   ├── dropbear
│   │   ├── authorized_keys
│   │   └── dropbear_rsa_host_key
│   ├── e2fsck.conf
│   ├── filesystems
│   ├── firewall.d
│   │   └── qca-nss-ecm
│   ├── fstab
│   ├── group
│   ├── hosts
│   ├── hotplug-preinit.json
│   ├── hotplug.d
│   │   ├── button
│   │   │   ├── 50-wps
│   │   │   ├── 51-wps-reset
│   │   │   ├── 52-wps-supplicant
│   │   │   └── 54-wps-extender
│   │   ├── firmware
│   │   │   └── 10-qca-nss-fw
│   │   ├── iface
│   │   │   ├── 00-netstate
│   │   │   ├── 15-teql
│   │   │   ├── 25-dnsmasq
│   │   │   ├── 50-miniupnpd
│   │   │   ├── 70-quagga
│   │   │   └── 90-rngd
│   │   ├── net
│   │   │   └── 00-sysctl
│   │   ├── ntp
│   │   │   └── 25-dnsmasqsec
│   │   └── tty
│   │       └── 01-hsuart
│   ├── hotplug.json
│   ├── init.d
│   │   ├── boot
│   │   ├── conntrackd
│   │   ├── cron
│   │   ├── dnsmasq
│   │   ├── done
│   │   ├── dropbear
│   │   ├── inetd
│   │   ├── led
│   │   ├── log
│   │   ├── macsec
│   │   ├── miniupnpd
│   │   ├── network
│   │   ├── ntp
│   │   ├── odhcpd
│   │   ├── powerctl
│   │   ├── qca-edma
│   │   ├── qca-hostapd
│   │   ├── qca-nss-drv
│   │   ├── qca-nss-ecm
│   │   ├── qca-ssdk
│   │   ├── qca-wpa-supplicant
│   │   ├── qcmbr
│   │   ├── qrfs
│   │   ├── quagga
│   │   ├── rngd
│   │   ├── sensord
│   │   ├── shortcut-fe
│   │   ├── skb_recycler
│   │   ├── ssid_steering
│   │   ├── switch_antenna
│   │   ├── sysctl
│   │   ├── sysfixtime
│   │   ├── sysntpd
│   │   ├── system
│   │   ├── telnet
│   │   ├── thermal
│   │   ├── umount
│   │   └── wifi_control
│   ├── inittab
│   ├── iproute2
│   │   └── rt_tables
│   ├── lowi
│   │   └── lowi.conf
│   ├── mal_default_cfg
│   │   ├── ddns.cfg
│   │   ├── dnsmasq.conf
│   │   ├── ethwan.cfg
│   │   ├── firewall.cfg
│   │   ├── firewall.sql
│   │   ├── lan.cfg
│   │   ├── mal.cfg
│   │   ├── malmanager.cfg
│   │   ├── overheat.cfg
│   │   ├── routing.cfg
│   │   ├── routing.sql
│   │   ├── system.sql
│   │   ├── systime.cfg
│   │   ├── vpn.cfg
│   │   ├── webui.cfg
│   │   └── wifi.cfg
│   ├── mm_config
│   ├── modules-boot.d
│   │   ├── 02-crypto-hash
│   │   ├── 04-crypto-crc32c
│   │   ├── 09-crypto-aead
│   │   ├── 30-button-hotplug
│   │   ├── 30-gpio-button-hotplug
│   │   ├── 40-scsi-core
│   │   ├── 50-ledtrig-timer
│   │   ├── 56-bootconfig
│   │   └── 60-leds-lp5562
│   ├── modules.d
│   │   ├── 02-crypto-hash
│   │   ├── 04-crypto-crc32c
│   │   ├── 09-crypto-aead
│   │   ├── 09-crypto-aes
│   │   ├── 09-crypto-arc4
│   │   ├── 09-crypto-authenc
│   │   ├── 09-crypto-cbc
│   │   ├── 09-crypto-deflate
│   │   ├── 09-crypto-des
│   │   ├── 09-crypto-ecb
│   │   ├── 09-crypto-hmac
│   │   ├── 09-crypto-md5
│   │   ├── 09-crypto-ocf
│   │   ├── 09-crypto-qcrypto
│   │   ├── 09-crypto-rng
│   │   ├── 09-crypto-sha1
│   │   ├── 09-crypto-wq
│   │   ├── 09-llc
│   │   ├── 09-shortcut-fe
│   │   ├── 10-aq_phy
│   │   ├── 10-crypto-iv
│   │   ├── 10-shortcut-fe-drv
│   │   ├── 10-stp
│   │   ├── 11-bridge
│   │   ├── 12-8021q
│   │   ├── 25-nls-cp437
│   │   ├── 25-nls-iso8859-1
│   │   ├── 29-qca-rfs
│   │   ├── 30-button-hotplug
│   │   ├── 30-fs-ntfs
│   │   ├── 30-fs-vfat
│   │   ├── 30-gpio-button-hotplug
│   │   ├── 30-ipsec
│   │   ├── 30-qca-ssdk-hnat
│   │   ├── 31-iptunnel
│   │   ├── 31-iptunnel4
│   │   ├── 31-iptunnel6
│   │   ├── 31-qca-nss-gmac
│   │   ├── 32-ip6-tunnel
│   │   ├── 32-ipsec4
│   │   ├── 32-ipsec6
│   │   ├── 32-l2tp
│   │   ├── 32-qca-nss-drv
│   │   ├── 32-udptunnel4
│   │   ├── 32-udptunnel6
│   │   ├── 33-nat46
│   │   ├── 39-gre
│   │   ├── 39-gre6
│   │   ├── 40-bonding
│   │   ├── 40-fs-msdos
│   │   ├── 40-qca_85xx_sw
│   │   ├── 40-scsi-core
│   │   ├── 41-qca-mcs
│   │   ├── 42-ip6tables
│   │   ├── 43-ip6tables-extra
│   │   ├── 43-ipt-nat6
│   │   ├── 45-qca-edma
│   │   ├── 50-ipt-ct-sctp
│   │   ├── 50-ledtrig-heartbeat
│   │   ├── 50-ledtrig-timer
│   │   ├── 51-i2c-core
│   │   ├── 51-nat-sctp
│   │   ├── 51-qca-nss-drv-gre
│   │   ├── 51-qca-nss-drv-l2tpv2
│   │   ├── 51-qca-nss-drv-lag-mgr
│   │   ├── 51-qca-nss-drv-pptp
│   │   ├── 52-qca-nss-crypto
│   │   ├── 52-qca-nss-macsec
│   │   ├── 56-bootconfig
│   │   ├── 58-qca-nss-drv-qdisc
│   │   ├── 59-qca-nss-cfi-cryptoapi
│   │   ├── 60-hwmon-tmp102
│   │   ├── 60-leds-lp5562
│   │   ├── 60-qca-nss-drv-ipsecmgr
│   │   ├── 61-qca-nss-cfi-ocf
│   │   ├── 70-sched-core
│   │   ├── 71-sched-connmark
│   │   ├── 73-sched
│   │   ├── 80-fuse
│   │   ├── arptables
│   │   ├── ipt-compat-xtables
│   │   ├── ipt-conntrack
│   │   ├── ipt-conntrack-extra
│   │   ├── ipt-core
│   │   ├── ipt-extra
│   │   ├── ipt-filter
│   │   ├── ipt-fullconenat
│   │   ├── ipt-iface
│   │   ├── ipt-ipmark
│   │   ├── ipt-ipopt
│   │   ├── ipt-ipp2p
│   │   ├── ipt-iprange
│   │   ├── ipt-ipsec
│   │   ├── ipt-nat
│   │   ├── ipt-nat-extra
│   │   ├── ipt-nathelper-rtsp
│   │   ├── lib-crc-ccitt
│   │   ├── lib-crc32c
│   │   ├── lib-textsearch
│   │   ├── lib-zlib
│   │   ├── mppe
│   │   ├── nf-conntrack
│   │   ├── nf-conntrack-netlink
│   │   ├── nf-conntrack6
│   │   ├── nf-ipt
│   │   ├── nf-ipt6
│   │   ├── nf-nat
│   │   ├── nf-nat6
│   │   ├── nf-nathelper
│   │   ├── nf-nathelper-extra
│   │   ├── nfnetlink
│   │   ├── nfnetlink-queue
│   │   ├── ppp
│   │   ├── pppoe
│   │   ├── pppol2tp
│   │   └── pptp
│   ├── mtab
│   ├── openwrt_release
│   ├── openwrt_version
│   ├── opkg
│   │   ├── customfeeds.conf
│   │   ├── distfeeds.conf
│   │   └── keys
│   │       ├── 53bad1233d4c98c5
│   │       ├── 5c254e292beefb4a
│   │       ├── a70eb20b0f9a42e7
│   │       └── de98a2dd1d0f8a07
│   ├── opkg.conf
│   ├── passwd
│   ├── pm
│   │   └── power.d
│   │       └── ipq-power-save.sh
│   ├── ppp
│   │   ├── chap-secrets
│   │   ├── filter
│   │   ├── ip-down
│   │   ├── ip-down.d
│   │   │   └── clear-tunnel-server-blackhole
│   │   ├── ip-up
│   │   ├── ip-up.d
│   │   │   └── add-tunnel-server-blackhole
│   │   ├── ipv6-up
│   │   ├── options
│   │   └── options.pptp
│   ├── preinit
│   ├── profile
│   ├── protocols
│   ├── quagga
│   │   ├── ripd.conf
│   │   └── zebra.conf
│   ├── rc.button
│   │   ├── failsafe
│   │   ├── power
│   │   ├── reset
│   │   └── rfkill
│   ├── rc.common
│   ├── rc.d
│   │   ├── K15miniupnpd
│   │   ├── K50dropbear
│   │   ├── K89log
│   │   ├── K90network
│   │   ├── K98boot
│   │   ├── K99umount
│   │   ├── S00sysfixtime
│   │   ├── S10boot
│   │   ├── S10system
│   │   ├── S11sysctl
│   │   ├── S12log
│   │   ├── S15qca-edma
│   │   ├── S15qca-hostapd
│   │   ├── S15qca-wpa-supplicant
│   │   ├── S16qca-ssdk
│   │   ├── S19qca-nss-ecm
│   │   ├── S20network
│   │   ├── S40skb_recycler
│   │   ├── S50dropbear
│   │   ├── S50wifi_control
│   │   ├── S60dnsmasq
│   │   ├── S60quagga
│   │   ├── S70qca-nss-drv
│   │   ├── S70qrfs
│   │   ├── S72shortcut-fe
│   │   ├── S95done
│   │   ├── S95miniupnpd
│   │   ├── S98ntp
│   │   ├── S98powerctl
│   │   ├── S98rngd
│   │   └── S98thermal
│   ├── rc.local
│   ├── resolv.conf
│   ├── services
│   ├── shadow
│   ├── shells
│   ├── spacex
│   │   ├── certs
│   │   └── keys
│   ├── ssl
│   │   ├── certs
│   │   │   ├── 02265526.0
│   │   │   ├── 024dc131.0
│   │   │   ├── 03179a64.0
│   │   │   ├── 034868d6.0
│   │   │   ├── 062cdee6.0
│   │   │   ├── 064e0aa9.0
│   │   │   ├── 080911ac.0
│   │   │   ├── 0810ba98.0
│   │   │   ├── 09789157.0
│   │   │   ├── 0b1b94ef.0
│   │   │   ├── 0c4c9b6c.0
│   │   │   ├── 0d1b923b.0
│   │   │   ├── 106f3e4d.0
│   │   │   ├── 116bf586.0
│   │   │   ├── 128805a3.0
│   │   │   ├── 157753a5.0
│   │   │   ├── 1636090b.0
│   │   │   ├── 1874d4aa.0
│   │   │   ├── 18856ac4.0
│   │   │   ├── 19c1fa33.0
│   │   │   ├── 1d3472b9.0
│   │   │   ├── 1e08bfd1.0
│   │   │   ├── 1e09d511.0
│   │   │   ├── 244b5494.0
│   │   │   ├── 24ad0b63.0
│   │   │   ├── 2ae6433e.0
│   │   │   ├── 2b349938.0
│   │   │   ├── 2c11d503.0
│   │   │   ├── 2c543cd1.0
│   │   │   ├── 2e4eed3c.0
│   │   │   ├── 2e5ac55d.0
│   │   │   ├── 32888f65.0
│   │   │   ├── 349f2832.0
│   │   │   ├── 3513523f.0
│   │   │   ├── 381ce4dd.0
│   │   │   ├── 3b2716e5.0
│   │   │   ├── 3bde41ac.0
│   │   │   ├── 3e45d192.0
│   │   │   ├── 3ee7e181.0
│   │   │   ├── 3efd4dc0.0
│   │   │   ├── 40193066.0
│   │   │   ├── 4042bcee.0
│   │   │   ├── 40547a79.0
│   │   │   ├── 415660c1.0
│   │   │   ├── 4304c5e5.0
│   │   │   ├── 442adcac.0
│   │   │   ├── 451b5485.0
│   │   │   ├── 480720ec.0
│   │   │   ├── 48bec511.0
│   │   │   ├── 4a6481c9.0
│   │   │   ├── 4bfab552.0
│   │   │   ├── 4f316efb.0
│   │   │   ├── 5273a94c.0
│   │   │   ├── 5443e9e3.0
│   │   │   ├── 54657681.0
│   │   │   ├── 5620c4aa.0
│   │   │   ├── 56657bde.0
│   │   │   ├── 578d5c04.0
│   │   │   ├── 57bbd831.0
│   │   │   ├── 57bcb2da.0
│   │   │   ├── 592c0a9a.0
│   │   │   ├── 5a4d6896.0
│   │   │   ├── 5ad8a5d6.0
│   │   │   ├── 5c44d531.0
│   │   │   ├── 5cd81ad7.0
│   │   │   ├── 5f15c80c.0
│   │   │   ├── 607986c7.0
│   │   │   ├── 608a55ad.0
│   │   │   ├── 6410666e.0
│   │   │   ├── 653b494a.0
│   │   │   ├── 65b876bd.0
│   │   │   ├── 667c66d4.0
│   │   │   ├── 6b99d060.0
│   │   │   ├── 6f2c1157.0
│   │   │   ├── 706f604c.0
│   │   │   ├── 749e9e03.0
│   │   │   ├── 75d1b2ed.0
│   │   │   ├── 76cb8f92.0
│   │   │   ├── 76faf6c0.0
│   │   │   ├── 7719f463.0
│   │   │   ├── 790a7190.0
│   │   │   ├── 7992b8bb.0
│   │   │   ├── 79ad8b43.0
│   │   │   ├── 7d0b38bd.0
│   │   │   ├── 7d5a75e4.0
│   │   │   ├── 7f3d5d1d.0
│   │   │   ├── 812e17de.0
│   │   │   ├── 8160b96c.0
│   │   │   ├── 861a399d.0
│   │   │   ├── 87229d21.0
│   │   │   ├── 8867006a.0
│   │   │   ├── 8b59b1ad.0
│   │   │   ├── 8d86cdd1.0
│   │   │   ├── 9007ae68.0
│   │   │   ├── 9168f543.0
│   │   │   ├── 930ac5d2.0
│   │   │   ├── 93bc0acc.0
│   │   │   ├── 988a38cb.0
│   │   │   ├── 9c2e7d30.0
│   │   │   ├── 9c8dfbd4.0
│   │   │   ├── 9d04f354.0
│   │   │   ├── 9d520b32.0
│   │   │   ├── 9f0f5fd6.0
│   │   │   ├── ACCVRAIZ1.crt
│   │   │   ├── ACEDICOM_Root.crt
│   │   │   ├── AC_Rai�\201z_Certica�\201mara_S.A..crt
│   │   │   ├── Actalis_Authentication_Root_CA.crt
│   │   │   ├── AddTrust_External_Root.crt
│   │   │   ├── AddTrust_Low-Value_Services_Root.crt
│   │   │   ├── AddTrust_Public_Services_Root.crt
│   │   │   ├── AddTrust_Qualified_Certificates_Root.crt
│   │   │   ├── AffirmTrust_Commercial.crt
│   │   │   ├── AffirmTrust_Networking.crt
│   │   │   ├── AffirmTrust_Premium.crt
│   │   │   ├── AffirmTrust_Premium_ECC.crt
│   │   │   ├── ApplicationCA_-_Japanese_Government.crt
│   │   │   ├── Atos_TrustedRoot_2011.crt
│   │   │   ├── Autoridad_de_Certificacion_Firmaprofesional_CIF_A62634068.crt
│   │   │   ├── Baltimore_CyberTrust_Root.crt
│   │   │   ├── Buypass_Class_2_CA_1.crt
│   │   │   ├── Buypass_Class_2_Root_CA.crt
│   │   │   ├── Buypass_Class_3_Root_CA.crt
│   │   │   ├── CA_Disig_Root_R1.crt
│   │   │   ├── CA_Disig_Root_R2.crt
│   │   │   ├── CFCA_EV_ROOT.crt
│   │   │   ├── CNNIC_ROOT.crt
│   │   │   ├── COMODO_Certification_Authority.crt
│   │   │   ├── COMODO_ECC_Certification_Authority.crt
│   │   │   ├── COMODO_RSA_Certification_Authority.crt
│   │   │   ├── Camerfirma_Chambers_of_Commerce_Root.crt
│   │   │   ├── Camerfirma_Global_Chambersign_Root.crt
│   │   │   ├── Certigna.crt
│   │   │   ├── Certinomis_-_Autorite�\201_Racine.crt
│   │   │   ├── Certinomis_-_Root_CA.crt
│   │   │   ├── Certplus_Class_2_Primary_CA.crt
│   │   │   ├── Certplus_Root_CA_G1.crt
│   │   │   ├── Certplus_Root_CA_G2.crt
│   │   │   ├── Certum_Root_CA.crt
│   │   │   ├── Certum_Trusted_Network_CA.crt
│   │   │   ├── Certum_Trusted_Network_CA_2.crt
│   │   │   ├── Chambers_of_Commerce_Root_-_2008.crt
│   │   │   ├── China_Internet_Network_Information_Center_EV_Certificates_Root.crt
│   │   │   ├── ComSign_CA.crt
│   │   │   ├── Comodo_AAA_Services_root.crt
│   │   │   ├── Comodo_Secure_Services_root.crt
│   │   │   ├── Comodo_Trusted_Services_root.crt
│   │   │   ├── Cybertrust_Global_Root.crt
│   │   │   ├── D-TRUST_Root_Class_3_CA_2_2009.crt
│   │   │   ├── D-TRUST_Root_Class_3_CA_2_EV_2009.crt
│   │   │   ├── DST_ACES_CA_X6.crt
│   │   │   ├── DST_Root_CA_X3.crt
│   │   │   ├── Deutsche_Telekom_Root_CA_2.crt
│   │   │   ├── DigiCert_Assured_ID_Root_CA.crt
│   │   │   ├── DigiCert_Assured_ID_Root_G2.crt
│   │   │   ├── DigiCert_Assured_ID_Root_G3.crt
│   │   │   ├── DigiCert_Global_Root_CA.crt
│   │   │   ├── DigiCert_Global_Root_G2.crt
│   │   │   ├── DigiCert_Global_Root_G3.crt
│   │   │   ├── DigiCert_High_Assurance_EV_Root_CA.crt
│   │   │   ├── DigiCert_Trusted_Root_G4.crt
│   │   │   ├── E-Tugra_Certification_Authority.crt
│   │   │   ├── EBG_Elektronik_Sertifika_Hizmet_Sag�\206layıcısı.crt
│   │   │   ├── EC-ACC.crt
│   │   │   ├── EE_Certification_Centre_Root_CA.crt
│   │   │   ├── Entrust.net_Premium_2048_Secure_Server_CA.crt
│   │   │   ├── Entrust_Root_Certification_Authority.crt
│   │   │   ├── Entrust_Root_Certification_Authority_-_EC1.crt
│   │   │   ├── Entrust_Root_Certification_Authority_-_G2.crt
│   │   │   ├── Equifax_Secure_CA.crt
│   │   │   ├── Equifax_Secure_Global_eBusiness_CA.crt
│   │   │   ├── Equifax_Secure_eBusiness_CA_1.crt
│   │   │   ├── GeoTrust_Global_CA.crt
│   │   │   ├── GeoTrust_Global_CA_2.crt
│   │   │   ├── GeoTrust_Primary_Certification_Authority.crt
│   │   │   ├── GeoTrust_Primary_Certification_Authority_-_G2.crt
│   │   │   ├── GeoTrust_Primary_Certification_Authority_-_G3.crt
│   │   │   ├── GeoTrust_Universal_CA.crt
│   │   │   ├── GeoTrust_Universal_CA_2.crt
│   │   │   ├── GlobalSign_ECC_Root_CA_-_R4.crt
│   │   │   ├── GlobalSign_ECC_Root_CA_-_R5.crt
│   │   │   ├── GlobalSign_Root_CA.crt
│   │   │   ├── GlobalSign_Root_CA_-_R2.crt
│   │   │   ├── GlobalSign_Root_CA_-_R3.crt
│   │   │   ├── Global_Chambersign_Root_-_2008.crt
│   │   │   ├── Go_Daddy_Class_2_CA.crt
│   │   │   ├── Go_Daddy_Root_Certificate_Authority_-_G2.crt
│   │   │   ├── Hellenic_Academic_and_Research_Institutions_ECC_RootCA_2015.crt
│   │   │   ├── Hellenic_Academic_and_Research_Institutions_RootCA_2011.crt
│   │   │   ├── Hellenic_Academic_and_Research_Institutions_RootCA_2015.crt
│   │   │   ├── Hongkong_Post_Root_CA_1.crt
│   │   │   ├── IGC_A.crt
│   │   │   ├── ISRG_Root_X1.crt
│   │   │   ├── IdenTrust_Commercial_Root_CA_1.crt
│   │   │   ├── IdenTrust_Public_Sector_Root_CA_1.crt
│   │   │   ├── Izenpe.com.crt
│   │   │   ├── Juur-SK.crt
│   │   │   ├── Microsec_e-Szigno_Root_CA.crt
│   │   │   ├── Microsec_e-Szigno_Root_CA_2009.crt
│   │   │   ├── NetLock_Arany_=Class_Gold=_Fo�\213tanu�\201si�\201tva�\201ny.crt
│   │   │   ├── Network_Solutions_Certificate_Authority.crt
│   │   │   ├── OISTE_WISeKey_Global_Root_GA_CA.crt
│   │   │   ├── OISTE_WISeKey_Global_Root_GB_CA.crt
│   │   │   ├── OpenTrust_Root_CA_G1.crt
│   │   │   ├── OpenTrust_Root_CA_G2.crt
│   │   │   ├── OpenTrust_Root_CA_G3.crt
│   │   │   ├── PSCProcert.crt
│   │   │   ├── QuoVadis_Root_CA.crt
│   │   │   ├── QuoVadis_Root_CA_1_G3.crt
│   │   │   ├── QuoVadis_Root_CA_2.crt
│   │   │   ├── QuoVadis_Root_CA_2_G3.crt
│   │   │   ├── QuoVadis_Root_CA_3.crt
│   │   │   ├── QuoVadis_Root_CA_3_G3.crt
│   │   │   ├── RSA_Security_2048_v3.crt
│   │   │   ├── Root_CA_Generalitat_Valenciana.crt
│   │   │   ├── S-TRUST_Authentication_and_Encryption_Root_CA_2005_PN.crt
│   │   │   ├── S-TRUST_Universal_Root_CA.crt
│   │   │   ├── SZAFIR_ROOT_CA2.crt
│   │   │   ├── SecureSign_RootCA11.crt
│   │   │   ├── SecureTrust_CA.crt
│   │   │   ├── Secure_Global_CA.crt
│   │   │   ├── Security_Communication_EV_RootCA1.crt
│   │   │   ├── Security_Communication_RootCA2.crt
│   │   │   ├── Security_Communication_Root_CA.crt
│   │   │   ├── Sonera_Class_2_Root_CA.crt
│   │   │   ├── Staat_der_Nederlanden_EV_Root_CA.crt
│   │   │   ├── Staat_der_Nederlanden_Root_CA_-_G2.crt
│   │   │   ├── Staat_der_Nederlanden_Root_CA_-_G3.crt
│   │   │   ├── Starfield_Class_2_CA.crt
│   │   │   ├── Starfield_Root_Certificate_Authority_-_G2.crt
│   │   │   ├── Starfield_Services_Root_Certificate_Authority_-_G2.crt
│   │   │   ├── SwissSign_Gold_CA_-_G2.crt
│   │   │   ├── SwissSign_Platinum_CA_-_G2.crt
│   │   │   ├── SwissSign_Silver_CA_-_G2.crt
│   │   │   ├── Swisscom_Root_CA_1.crt
│   │   │   ├── Swisscom_Root_CA_2.crt
│   │   │   ├── Swisscom_Root_EV_CA_2.crt
│   │   │   ├── T-TeleSec_GlobalRoot_Class_2.crt
│   │   │   ├── T-TeleSec_GlobalRoot_Class_3.crt
│   │   │   ├── TC_TrustCenter_Class_3_CA_II.crt
│   │   │   ├── TURKTRUST_Certificate_Services_Provider_Root_2007.crt
│   │   │   ├── TU�\210BI�\207TAK_UEKAE_Ko�\210k_Sertifika_Hizmet_Sag�\206layıcısı_-_Su�\210ru�\210m_3.crt
│   │   │   ├── TU�\210RKTRUST_Elektronik_Sertifika_Hizmet_Sag�\206layıcısı_H5.crt
│   │   │   ├── TU�\210RKTRUST_Elektronik_Sertifika_Hizmet_Sag�\206layıcısı_H6.crt
│   │   │   ├── TWCA_Global_Root_CA.crt
│   │   │   ├── TWCA_Root_Certification_Authority.crt
│   │   │   ├── Taiwan_GRCA.crt
│   │   │   ├── TeliaSonera_Root_CA_v1.crt
│   │   │   ├── Trustis_FPS_Root_CA.crt
│   │   │   ├── USERTrust_ECC_Certification_Authority.crt
│   │   │   ├── USERTrust_RSA_Certification_Authority.crt
│   │   │   ├── UTN_USERFirst_Email_Root_CA.crt
│   │   │   ├── UTN_USERFirst_Hardware_Root_CA.crt
│   │   │   ├── VeriSign_Class_3_Public_Primary_Certification_Authority_-_G4.crt
│   │   │   ├── VeriSign_Class_3_Public_Primary_Certification_Authority_-_G5.crt
│   │   │   ├── VeriSign_Universal_Root_Certification_Authority.crt
│   │   │   ├── Verisign_Class_1_Public_Primary_Certification_Authority.crt
│   │   │   ├── Verisign_Class_1_Public_Primary_Certification_Authority_-_G3.crt
│   │   │   ├── Verisign_Class_2_Public_Primary_Certification_Authority_-_G2.crt
│   │   │   ├── Verisign_Class_2_Public_Primary_Certification_Authority_-_G3.crt
│   │   │   ├── Verisign_Class_3_Public_Primary_Certification_Authority.crt
│   │   │   ├── Verisign_Class_3_Public_Primary_Certification_Authority_-_G3.crt
│   │   │   ├── Visa_eCommerce_Root.crt
│   │   │   ├── WellsSecure_Public_Root_Certificate_Authority.crt
│   │   │   ├── XRamp_Global_CA_Root.crt
│   │   │   ├── a760e1bd.0
│   │   │   ├── a8dee976.0
│   │   │   ├── a94d09e5.0
│   │   │   ├── ad088e1d.0
│   │   │   ├── aee5f10d.0
│   │   │   ├── b0e59380.0
│   │   │   ├── b1159c4c.0
│   │   │   ├── b13cc6df.0
│   │   │   ├── b1b8a7f3.0
│   │   │   ├── b204d74a.0
│   │   │   ├── b66938e9.0
│   │   │   ├── b727005e.0
│   │   │   ├── b7a5b843.0
│   │   │   ├── ba89ed3b.0
│   │   │   ├── bb2d49a0.0
│   │   │   ├── bd1910d4.0
│   │   │   ├── c01cdfa2.0
│   │   │   ├── c089bbbd.0
│   │   │   ├── c0ff1f52.0
│   │   │   ├── c28a8a30.0
│   │   │   ├── c47d9980.0
│   │   │   ├── c5d3212a.0
│   │   │   ├── c5e082db.0
│   │   │   ├── c679bc3f.0
│   │   │   ├── c99398f3.0
│   │   │   ├── c9f83a1c.0
│   │   │   ├── ca6e4ad9.0
│   │   │   ├── cb357862.0
│   │   │   ├── cb59f961.0
│   │   │   ├── cbeee9e2.0
│   │   │   ├── cbf06781.0
│   │   │   ├── cc450945.0
│   │   │   ├── cd58d51e.0
│   │   │   ├── certSIGN_ROOT_CA.crt
│   │   │   ├── cfa1c2ee.0
│   │   │   ├── d4dae3dd.0
│   │   │   ├── d6325660.0
│   │   │   ├── d7e8dc79.0
│   │   │   ├── d853d49e.0
│   │   │   ├── d957f522.0
│   │   │   ├── dc45b0bd.0
│   │   │   ├── dd8e9d41.0
│   │   │   ├── e113c810.0
│   │   │   ├── e18bfb83.0
│   │   │   ├── e2799e36.0
│   │   │   ├── e36a6752.0
│   │   │   ├── e536d871.0
│   │   │   ├── e73d606e.0
│   │   │   ├── e8de2f56.0
│   │   │   ├── ePKI_Root_Certification_Authority.crt
│   │   │   ├── ee1365c0.0
│   │   │   ├── ee64a828.0
│   │   │   ├── eed8c118.0
│   │   │   ├── ef2f636c.0
│   │   │   ├── ef954a4e.0
│   │   │   ├── f060240e.0
│   │   │   ├── f081611a.0
│   │   │   ├── f30dd6ad.0
│   │   │   ├── f3377b1b.0
│   │   │   ├── f387163d.0
│   │   │   ├── f39fc864.0
│   │   │   ├── f90208f7.0
│   │   │   ├── fc5a8f99.0
│   │   │   ├── fcac10e3.0
│   │   │   ├── fe8a2cd8.0
│   │   │   ├── thawte_Primary_Root_CA.crt
│   │   │   ├── thawte_Primary_Root_CA_-_G2.crt
│   │   │   └── thawte_Primary_Root_CA_-_G3.crt
│   │   ├── openssl.cnf
│   │   └── private
│   ├── sysctl.conf
│   ├── sysctl.d
│   │   ├── qca-nss-drv.conf
│   │   └── qca-nss-ecm.conf
│   ├── sysupgrade.conf
│   ├── thermal
│   │   ├── ipq-thermald-8064.conf
│   │   ├── ipq-thermald-8066.conf
│   │   └── ipq-thermald-8069.conf
│   ├── uci-defaults
│   │   ├── 10_migrate-shadow
│   │   ├── 11_migrate-sysctl
│   │   ├── 12_network-generate-ula
│   │   ├── 20_migrate-feeds
│   │   ├── 30_uboot-envtools
│   │   ├── 99-miniupnpd
│   │   ├── 99-qca-nss-ecm
│   │   ├── network
│   │   ├── odhcpd.defaults
│   │   └── skb_recycler
│   ├── version
│   └── www
│       ├── static
│       │   ├── css
│       │   │   ├── layout.css
│       │   │   └── normalize.min.css
│       │   ├── favicon.ico
│       │   ├── fonts
│       │   │   └── D-DIN
│       │   │       ├── COPYING.txt
│       │   │       ├── D-DIN-Bold.otf
│       │   │       ├── D-DIN-Bold.ttf
│       │   │       ├── D-DIN-Bold.woff
│       │   │       ├── D-DIN-Bold.woff2
│       │   │       ├── D-DIN.otf
│       │   │       ├── D-DIN.ttf
│       │   │       ├── D-DIN.woff
│       │   │       ├── D-DIN.woff2
│       │   │       ├── FONTLOG.txt
│       │   │       ├── OFL-1.1.txt
│       │   │       └── README
│       │   ├── images
│       │   │   └── regulatory_label.png
│       │   └── js
│       │       └── core.js
│       └── templates
│           ├── captive_portal.html
│           ├── form.html
│           ├── regulatory_label.html
│           └── success.html
├── init
├── lib
│   ├── config
│   │   └── uci.sh
│   ├── debug
│   │   ├── power
│   │   ├── qca-nss-drv
│   │   ├── system
│   │   └── tc
│   ├── firmware
│   │   ├── AR9887
│   │   │   ├── athwlan.bin
│   │   │   ├── boardData_4_QC98XX_xb241_gld.bin
│   │   │   ├── boardData_4_QC98XX_xb243_gld.bin
│   │   │   ├── boarddata_0.bin
│   │   │   ├── boarddata_0_xb242.bin
│   │   │   ├── fakeBoardData_AR6004.bin
│   │   │   ├── otp.bin
│   │   │   └── utf.bin
│   │   ├── AR9888
│   │   │   └── hw.2
│   │   │       ├── atf.bin
│   │   │       ├── athwlan.bin
│   │   │       ├── boardData_2_QC98XX_cus223_523_gld.bin
│   │   │       ├── boardData_2_QC98XX_xb143_gld.bin
│   │   │       ├── boardData_3_QC98XX_cus261_gld.bin
│   │   │       ├── boardData_3_QC98XX_xb141_gld.bin
│   │   │       ├── fakeBoardData_AR6004.bin
│   │   │       ├── lteu.bin
│   │   │       ├── otp.bin
│   │   │       └── utf.bin
│   │   ├── IPQ4019
│   │   │   └── hw.1
│   │   │       ├── AR
│   │   │       │   ├── boardData_1_0_IPQ4019_Y9803_wifi0.bin
│   │   │       │   ├── boardData_1_0_IPQ4019_Y9803_wifi1.bin
│   │   │       │   ├── boarddata_0.bin
│   │   │       │   └── boarddata_1.bin
│   │   │       ├── AU
│   │   │       │   ├── boardData_1_0_IPQ4019_Y9803_wifi0.bin
│   │   │       │   ├── boardData_1_0_IPQ4019_Y9803_wifi1.bin
│   │   │       │   ├── boarddata_0.bin
│   │   │       │   └── boarddata_1.bin
│   │   │       ├── CA
│   │   │       │   ├── boardData_1_0_IPQ4019_Y9803_wifi0.bin
│   │   │       │   ├── boardData_1_0_IPQ4019_Y9803_wifi1.bin
│   │   │       │   ├── boarddata_0.bin
│   │   │       │   └── boarddata_1.bin
│   │   │       ├── CL
│   │   │       │   ├── boardData_1_0_IPQ4019_Y9803_wifi0.bin
│   │   │       │   ├── boardData_1_0_IPQ4019_Y9803_wifi1.bin
│   │   │       │   ├── boarddata_0.bin
│   │   │       │   └── boarddata_1.bin
│   │   │       ├── Global
│   │   │       │   ├── boardData_1_0_IPQ4019_Y9803_wifi0.bin
│   │   │       │   ├── boardData_1_0_IPQ4019_Y9803_wifi1.bin
│   │   │       │   ├── boarddata_0.bin
│   │   │       │   └── boarddata_1.bin
│   │   │       ├── NZ
│   │   │       │   ├── boardData_1_0_IPQ4019_Y9803_wifi0.bin
│   │   │       │   ├── boardData_1_0_IPQ4019_Y9803_wifi1.bin
│   │   │       │   ├── boarddata_0.bin
│   │   │       │   └── boarddata_1.bin
│   │   │       ├── README.md
│   │   │       ├── US_UK_JP
│   │   │       │   ├── boardData_1_0_IPQ4019_Y9803_wifi0.bin
│   │   │       │   ├── boardData_1_0_IPQ4019_Y9803_wifi1.bin
│   │   │       │   ├── boarddata_0.bin
│   │   │       │   └── boarddata_1.bin
│   │   │       ├── athwlan.bin
│   │   │       ├── athwlan.codeswap.bin
│   │   │       ├── boardData_1_0_IPQ4019_DK01_2G.bin
│   │   │       ├── boardData_1_0_IPQ4019_DK01_5G.bin
│   │   │       ├── boardData_1_0_IPQ4019_DK03_wifi0.bin
│   │   │       ├── boardData_1_0_IPQ4019_DK03_wifi1.bin
│   │   │       ├── boardData_1_0_IPQ4019_DK04_2G.bin
│   │   │       ├── boardData_1_0_IPQ4019_DK04_2G_neg_pwr.bin
│   │   │       ├── boardData_1_0_IPQ4019_DK04_5G.bin
│   │   │       ├── boardData_1_0_IPQ4019_DK04_5G_neg_pwr.bin
│   │   │       ├── boardData_1_0_IPQ4019_DK05_2G.bin
│   │   │       ├── boardData_1_0_IPQ4019_DK05_5G.bin
│   │   │       ├── boardData_1_0_IPQ4019_DK06_2G.bin
│   │   │       ├── boardData_1_0_IPQ4019_DK06_5G.bin
│   │   │       ├── boardData_1_0_IPQ4019_DK07_wifi0_2G.bin
│   │   │       ├── boardData_1_0_IPQ4019_DK07_wifi0_5G_HB.bin
│   │   │       ├── boardData_1_0_IPQ4019_DK07_wifi1_5G_LB.bin
│   │   │       ├── boardData_1_0_IPQ4019_DK08_wifi0_2G.bin
│   │   │       ├── boardData_1_0_IPQ4019_DK08_wifi1_5G_LB.bin
│   │   │       ├── boardData_1_0_IPQ4019_Y9803_wifi0.bin
│   │   │       ├── boardData_1_0_IPQ4019_Y9803_wifi1.bin
│   │   │       ├── boardData_1_0_IPQ4019_YA131_wifi0.bin
│   │   │       ├── boardData_1_0_IPQ4019_YA131_wifi1.bin
│   │   │       ├── boarddata_0.bin
│   │   │       ├── boarddata_1.bin
│   │   │       ├── otp.bin
│   │   │       ├── utf.bin
│   │   │       └── utf.codeswap.bin
│   │   ├── QCA9888
│   │   │   └── hw.2
│   │   │       ├── athwlan.bin
│   │   │       ├── athwlan.codeswap.bin
│   │   │       ├── boardData_2_0_QCA9888_5G_Y9484.bin
│   │   │       ├── boardData_2_0_QCA9888_5G_Y9582.bin
│   │   │       ├── boardData_2_0_QCA9888_5G_Y9582_ETSI.bin
│   │   │       ├── boardData_2_0_QCA9888_5G_Y9690.bin
│   │   │       ├── boardData_2_0_QCA9888_5G_Y9690_SBS_HB.bin
│   │   │       ├── boardData_2_0_QCA9888_5G_YA105.bin
│   │   │       ├── boardData_2_0_QCA9888_5G_YA841.bin
│   │   │       ├── boarddata_0.bin
│   │   │       ├── boarddata_1.bin
│   │   │       ├── otp.bin
│   │   │       ├── utf.bin
│   │   │       └── utf.codeswap.bin
│   │   └── QCA9984
│   │       └── hw.1
│   │           ├── athwlan.bin
│   │           ├── athwlan.codeswap.bin
│   │           ├── boardData_QCA9984_CAS02_5G_YB921_v1_013.bin
│   │           ├── boardData_QCA9984_CAS02_high_band_5G_YB921_v1_014.bin
│   │           ├── boardData_QCA9984_CAS03_dual_band_5G_2G_YC325_v1_017.bin
│   │           ├── boardData_QCA9984_CUS238_5G_v1_003.bin
│   │           ├── boardData_QCA9984_CUS238_5G_v1_003_CTL.bin
│   │           ├── boardData_QCA9984_CUS239_5G_v1_001.bin
│   │           ├── boardData_QCA9984_CUS239_5G_v1_001_ctl.bin
│   │           ├── boardData_QCA9984_CUS239_dual_band_5G_YC325.bin
│   │           ├── boardData_QCA9984_CUS239_high_band_5G_v1_006.bin
│   │           ├── boardData_QCA9984_CUS239_low_band_5G_v1_005.bin
│   │           ├── boardData_QCA9984_CUS239_low_pwr_pa_5G_v1_007.bin
│   │           ├── boardData_QCA9984_CUS239_negative_pwr_offset_5G_v1_008.bin
│   │           ├── boardData_QCA9984_CUS240_2G_3x3_v1_010.bin
│   │           ├── boardData_QCA9984_CUS240_2G_v1_004.bin
│   │           ├── boardData_QCA9984_CUS240_2G_v1_004_CTL.bin
│   │           ├── boardData_QCA9984_CUS260_2G_v1_002.bin
│   │           ├── boardData_QCA9984_CUS260_2G_v1_002_ctl.bin
│   │           ├── boardData_QCA9984_CUS260_dual_band_2G_YC325.bin
│   │           ├── boardData_QCA9984_CUS260_negative_pwr_offset_2G_v1_009.bin
│   │           ├── boardData_QCA9986_CAS05_3x3_80M_5G_v1_015.bin
│   │           ├── boardData_QCA9988_CAS04_4x4_80M_5G_v1_016.bin
│   │           ├── boarddata_0.bin
│   │           ├── boarddata_1.bin
│   │           ├── ext_boardData_QCA9984_CAS03_dual_band_5G_2G_YC325_v1_001.bin
│   │           ├── otp.bin
│   │           ├── utf.bin
│   │           ├── utf.codeswap.bin
│   │           └── waltest.codeswap.bin
│   ├── functions
│   │   ├── fsck
│   │   │   └── e2fsck.sh
│   │   ├── leds.sh
│   │   ├── network.sh
│   │   ├── preinit.sh
│   │   ├── procd.sh
│   │   ├── service.sh
│   │   ├── system.sh
│   │   ├── uci-defaults-new.sh
│   │   └── uci-defaults.sh
│   ├── functions.sh
│   ├── ipq806x.sh
│   ├── ld-uClibc-1.0.14.so
│   ├── ld-uClibc.so.0
│   ├── ld-uClibc.so.1
│   ├── libblobmsg_json.so
│   ├── libc.so.1
│   ├── libcrypt-1.0.14.so
│   ├── libcrypt.so.1
│   ├── libdl-1.0.14.so
│   ├── libdl.so.1
│   ├── libfstools.so
│   ├── libgcc_s.so.1
│   ├── libjson_script.so
│   ├── libm-1.0.14.so
│   ├── libm.so.1
│   ├── libpthread-1.0.14.so
│   ├── libpthread.so.1
│   ├── librpc.so
│   ├── librt-1.0.14.so
│   ├── librt.so.1
│   ├── libsetlbf.so
│   ├── libssp.so.0
│   ├── libssp.so.0.0.0
│   ├── libuClibc-1.0.14.so
│   ├── libubox.so
│   ├── libubus.so
│   ├── libuci.so
│   ├── libutil-1.0.14.so
│   ├── libutil.so.1
│   ├── libvalidate.so
│   ├── modules
│   │   └── 4.4.60
│   │       ├── act_connmark.ko
│   │       ├── act_ipt.ko
│   │       ├── act_mirred.ko
│   │       ├── act_police.ko
│   │       ├── act_skbedit.ko
│   │       ├── af_key.ko
│   │       ├── ah4.ko
│   │       ├── ah6.ko
│   │       ├── aq_phy.ko
│   │       ├── arp_tables.ko
│   │       ├── arpt_mangle.ko
│   │       ├── arptable_filter.ko
│   │       ├── asf.ko
│   │       ├── ath_dev.ko
│   │       ├── ath_dfs.ko
│   │       ├── ath_hal.ko
│   │       ├── ath_pktlog.ko
│   │       ├── ath_rate_atheros.ko
│   │       ├── ath_spectral.ko
│   │       ├── authenc.ko
│   │       ├── bonding.ko
│   │       ├── bootconfig.ko
│   │       ├── button-hotplug.ko
│   │       ├── cbc.ko
│   │       ├── cls_basic.ko
│   │       ├── cls_flow.ko
│   │       ├── cls_fw.ko
│   │       ├── cls_route.ko
│   │       ├── cls_tcindex.ko
│   │       ├── cls_u32.ko
│   │       ├── compat_xtables.ko
│   │       ├── crc-ccitt.ko
│   │       ├── cryptodev.ko
│   │       ├── cryptosoft.ko
│   │       ├── des_generic.ko
│   │       ├── ecb.ko
│   │       ├── ecm.ko
│   │       ├── em_cmp.ko
│   │       ├── em_meta.ko
│   │       ├── em_nbyte.ko
│   │       ├── em_text.ko
│   │       ├── em_u32.ko
│   │       ├── esp4.ko
│   │       ├── esp6.ko
│   │       ├── essedma.ko
│   │       ├── fat.ko
│   │       ├── fuse.ko
│   │       ├── gpio-button-hotplug.ko
│   │       ├── gre.ko
│   │       ├── hst_tx99.ko
│   │       ├── hwmon.ko
│   │       ├── input-core.ko
│   │       ├── ip6_gre.ko
│   │       ├── ip6_tables.ko
│   │       ├── ip6_tunnel.ko
│   │       ├── ip6_udp_tunnel.ko
│   │       ├── ip6t_MASQUERADE.ko
│   │       ├── ip6t_NPT.ko
│   │       ├── ip6t_REJECT.ko
│   │       ├── ip6t_ah.ko
│   │       ├── ip6t_eui64.ko
│   │       ├── ip6t_frag.ko
│   │       ├── ip6t_hbh.ko
│   │       ├── ip6t_ipv6header.ko
│   │       ├── ip6t_mh.ko
│   │       ├── ip6t_rt.ko
│   │       ├── ip6table_filter.ko
│   │       ├── ip6table_mangle.ko
│   │       ├── ip6table_nat.ko
│   │       ├── ip6table_raw.ko
│   │       ├── ip_gre.ko
│   │       ├── ip_tables.ko
│   │       ├── ip_tunnel.ko
│   │       ├── ipcomp.ko
│   │       ├── ipcomp6.ko
│   │       ├── ipt_ECN.ko
│   │       ├── ipt_MASQUERADE.ko
│   │       ├── ipt_REJECT.ko
│   │       ├── ipt_ah.ko
│   │       ├── iptable_filter.ko
│   │       ├── iptable_mangle.ko
│   │       ├── iptable_nat.ko
│   │       ├── iptable_raw.ko
│   │       ├── l2tp_core.ko
│   │       ├── l2tp_netlink.ko
│   │       ├── l2tp_ppp.ko
│   │       ├── ledtrig-heartbeat.ko
│   │       ├── libcrc32c.ko
│   │       ├── md5.ko
│   │       ├── mem_manager.ko
│   │       ├── msdos.ko
│   │       ├── nat46.ko
│   │       ├── nf_conntrack.ko
│   │       ├── nf_conntrack_amanda.ko
│   │       ├── nf_conntrack_broadcast.ko
│   │       ├── nf_conntrack_ftp.ko
│   │       ├── nf_conntrack_h323.ko
│   │       ├── nf_conntrack_ipv4.ko
│   │       ├── nf_conntrack_ipv6.ko
│   │       ├── nf_conntrack_irc.ko
│   │       ├── nf_conntrack_netlink.ko
│   │       ├── nf_conntrack_pptp.ko
│   │       ├── nf_conntrack_proto_gre.ko
│   │       ├── nf_conntrack_proto_sctp.ko
│   │       ├── nf_conntrack_rtcache.ko
│   │       ├── nf_conntrack_rtsp.ko
│   │       ├── nf_conntrack_sip.ko
│   │       ├── nf_conntrack_snmp.ko
│   │       ├── nf_conntrack_tftp.ko
│   │       ├── nf_defrag_ipv4.ko
│   │       ├── nf_defrag_ipv6.ko
│   │       ├── nf_log_common.ko
│   │       ├── nf_log_ipv4.ko
│   │       ├── nf_log_ipv6.ko
│   │       ├── nf_nat.ko
│   │       ├── nf_nat_amanda.ko
│   │       ├── nf_nat_ftp.ko
│   │       ├── nf_nat_h323.ko
│   │       ├── nf_nat_ipv4.ko
│   │       ├── nf_nat_ipv6.ko
│   │       ├── nf_nat_irc.ko
│   │       ├── nf_nat_masquerade_ipv4.ko
│   │       ├── nf_nat_masquerade_ipv6.ko
│   │       ├── nf_nat_pptp.ko
│   │       ├── nf_nat_proto_gre.ko
│   │       ├── nf_nat_proto_sctp.ko
│   │       ├── nf_nat_redirect.ko
│   │       ├── nf_nat_rtsp.ko
│   │       ├── nf_nat_sip.ko
│   │       ├── nf_nat_snmp_basic.ko
│   │       ├── nf_nat_tftp.ko
│   │       ├── nf_reject_ipv4.ko
│   │       ├── nf_reject_ipv6.ko
│   │       ├── nfnetlink.ko
│   │       ├── nfnetlink_queue.ko
│   │       ├── nls_base.ko
│   │       ├── nls_cp437.ko
│   │       ├── nls_iso8859-1.ko
│   │       ├── ntfs.ko
│   │       ├── ocf.ko
│   │       ├── ppp_async.ko
│   │       ├── ppp_generic.ko
│   │       ├── ppp_mppe.ko
│   │       ├── pppoe.ko
│   │       ├── pppox.ko
│   │       ├── pptp.ko
│   │       ├── qca-mcs.ko
│   │       ├── qca-nss-cfi-cryptoapi.ko
│   │       ├── qca-nss-cfi-ocf.ko
│   │       ├── qca-nss-crypto-tool.ko
│   │       ├── qca-nss-crypto.ko
│   │       ├── qca-nss-drv.ko
│   │       ├── qca-nss-gmac.ko
│   │       ├── qca-nss-gre-test.ko
│   │       ├── qca-nss-gre.ko
│   │       ├── qca-nss-ipsec.ko
│   │       ├── qca-nss-ipsecmgr.ko
│   │       ├── qca-nss-l2tpv2.ko
│   │       ├── qca-nss-lag-mgr.ko
│   │       ├── qca-nss-macsec.ko
│   │       ├── qca-nss-pptp.ko
│   │       ├── qca-nss-profile-drv.ko
│   │       ├── qca-nss-qdisc.ko
│   │       ├── qca-ssdk.ko
│   │       ├── qca_85xx_sw.ko
│   │       ├── qca_da.ko
│   │       ├── qca_ol.ko
│   │       ├── qcedev.ko
│   │       ├── qcrypto.ko
│   │       ├── qdf.ko
│   │       ├── qrfs.ko
│   │       ├── sch_codel.ko
│   │       ├── sch_dsmark.ko
│   │       ├── sch_fq.ko
│   │       ├── sch_gred.ko
│   │       ├── sch_hfsc.ko
│   │       ├── sch_htb.ko
│   │       ├── sch_ingress.ko
│   │       ├── sch_pie.ko
│   │       ├── sch_prio.ko
│   │       ├── sch_red.ko
│   │       ├── sch_sfq.ko
│   │       ├── sch_tbf.ko
│   │       ├── sch_teql.ko
│   │       ├── sd_mod.ko
│   │       ├── sha1_generic.ko
│   │       ├── shortcut-fe-cm.ko
│   │       ├── shortcut-fe-drv.ko
│   │       ├── shortcut-fe-ipv6.ko
│   │       ├── shortcut-fe.ko
│   │       ├── slhc.ko
│   │       ├── smart_antenna.ko
│   │       ├── tmp102.ko
│   │       ├── ts_bm.ko
│   │       ├── ts_fsm.ko
│   │       ├── ts_kmp.ko
│   │       ├── tunnel4.ko
│   │       ├── tunnel6.ko
│   │       ├── udp_tunnel.ko
│   │       ├── umac.ko
│   │       ├── vfat.ko
│   │       ├── x_tables.ko
│   │       ├── xfrm4_mode_beet.ko
│   │       ├── xfrm4_mode_transport.ko
│   │       ├── xfrm4_mode_tunnel.ko
│   │       ├── xfrm4_tunnel.ko
│   │       ├── xfrm6_mode_beet.ko
│   │       ├── xfrm6_mode_transport.ko
│   │       ├── xfrm6_mode_tunnel.ko
│   │       ├── xfrm6_tunnel.ko
│   │       ├── xfrm_algo.ko
│   │       ├── xfrm_ipcomp.ko
│   │       ├── xfrm_user.ko
│   │       ├── xt_CLASSIFY.ko
│   │       ├── xt_CT.ko
│   │       ├── xt_DSCP.ko
│   │       ├── xt_FULLCONENAT.ko
│   │       ├── xt_HL.ko
│   │       ├── xt_IPMARK.ko
│   │       ├── xt_LOG.ko
│   │       ├── xt_NETMAP.ko
│   │       ├── xt_REDIRECT.ko
│   │       ├── xt_TCPMSS.ko
│   │       ├── xt_addrtype.ko
│   │       ├── xt_comment.ko
│   │       ├── xt_connbytes.ko
│   │       ├── xt_connlimit.ko
│   │       ├── xt_connmark.ko
│   │       ├── xt_conntrack.ko
│   │       ├── xt_ecn.ko
│   │       ├── xt_esp.ko
│   │       ├── xt_helper.ko
│   │       ├── xt_id.ko
│   │       ├── xt_iface.ko
│   │       ├── xt_ipp2p.ko
│   │       ├── xt_iprange.ko
│   │       ├── xt_length.ko
│   │       ├── xt_limit.ko
│   │       ├── xt_mac.ko
│   │       ├── xt_mark.ko
│   │       ├── xt_multiport.ko
│   │       ├── xt_nat.ko
│   │       ├── xt_owner.ko
│   │       ├── xt_physdev.ko
│   │       ├── xt_pkttype.ko
│   │       ├── xt_policy.ko
│   │       ├── xt_quota.ko
│   │       ├── xt_recent.ko
│   │       ├── xt_state.ko
│   │       ├── xt_statistic.ko
│   │       ├── xt_string.ko
│   │       ├── xt_tcpudp.ko
│   │       └── xt_time.ko
│   ├── netifd
│   │   ├── dhcp.script
│   │   ├── dhcpv6.script
│   │   ├── netifd-proto.sh
│   │   ├── netifd-wireless.sh
│   │   ├── offload
│   │   │   └── on-demand-down
│   │   ├── ppp-down
│   │   ├── ppp-up
│   │   ├── proto
│   │   │   ├── dhcp.sh
│   │   │   ├── dhcpv6.sh
│   │   │   └── ppp.sh
│   │   └── utils.sh
│   ├── network
│   │   ├── config.sh
│   │   └── switch.sh
│   ├── preinit
│   │   ├── 02_default_set_state
│   │   ├── 03_preinit_do_ipq806x.sh
│   │   ├── 10_indicate_failsafe
│   │   ├── 10_indicate_preinit
│   │   ├── 10_sysinfo
│   │   ├── 30_failsafe_wait
│   │   ├── 40_run_failsafe_hook
│   │   ├── 50_indicate_regular_preinit
│   │   ├── 70_initramfs_test
│   │   ├── 80_mount_root
│   │   ├── 81_load_wifi_board_bin
│   │   ├── 99_10_failsafe_login
│   │   └── 99_10_run_init
│   ├── read_caldata_to_fs.sh
│   ├── sbin
│   │   └── wifi_try
│   ├── uboot-envtools.sh
│   ├── update_smp_affinity.sh
│   ├── update_system_params.sh
│   ├── upgrade
│   │   ├── common.sh
│   │   ├── keep.d
│   │   │   ├── base-files
│   │   │   ├── base-files-essential
│   │   │   ├── inadyn
│   │   │   ├── lm-sensors
│   │   │   ├── opkg
│   │   │   ├── ppp
│   │   │   └── uboot-envtools
│   │   ├── nand.sh
│   │   └── platform.sh
│   └── wifi
│       ├── debug
│       │   ├── counters_wlan_prompt_akronite.sh
│       │   └── counters_wlan_prompt_dakota.sh
│       ├── dpp-hostapd-update-uci
│       ├── hostapd.sh
│       ├── icm.sh
│       ├── iface_mgr.sh
│       ├── lowi.sh
│       ├── qca-wifi-modules
│       ├── qcawifi.sh
│       ├── qcawifi_countrycode.txt
│       ├── wpa_supplicant.sh
│       ├── wps-hostapd-nbh-update
│       ├── wps-hostapd-update-uci
│       └── wps-supplicant-update-uci
├── mnt
├── overlay
├── proc
├── rom
│   └── note
├── root
├── sbin
│   ├── arp
│   ├── askfirst
│   ├── depmod
│   ├── devmem
│   ├── devstatus
│   ├── firstboot
│   ├── halt
│   ├── hotplug-call
│   ├── hwclock
│   ├── ifconfig
│   ├── ifdown
│   ├── ifstatus
│   ├── ifup
│   ├── init
│   ├── insmod
│   ├── jffs2mark
│   ├── jffs2reset
│   ├── kmodloader
│   ├── led.sh
│   ├── logd
│   ├── logread
│   ├── lsmod
│   ├── mkswap
│   ├── modinfo
│   ├── modprobe
│   ├── mount.ntfs-3g
│   ├── mount_root
│   ├── mtd
│   ├── netifd
│   ├── on_ac_power
│   ├── pivot_root
│   ├── poweroff
│   ├── procd
│   ├── reboot
│   ├── reload_config
│   ├── replace_BDF.sh
│   ├── rmmod
│   ├── rngd
│   ├── route
│   ├── setmac
│   ├── setup_iptables.sh
│   ├── snapshot
│   ├── snapshot_tool
│   ├── start-stop-daemon
│   ├── swconfig
│   ├── switch_root
│   ├── sysctl
│   ├── sysdebug
│   ├── syslogd
│   ├── sysupgrade
│   ├── tcpdump
│   ├── ubusd
│   ├── uci
│   ├── udevtrigger
│   ├── udhcpc
│   ├── upgraded
│   ├── validate_data
│   ├── vconfig
│   └── wifi
├── sys
├── tmp
├── usr
│   ├── bin
│   │   ├── [
│   │   ├── [[
│   │   ├── awk
│   │   ├── basename
│   │   ├── bunzip2
│   │   ├── bzcat
│   │   ├── c_rehash
│   │   ├── clear
│   │   ├── cmp
│   │   ├── crontab
│   │   ├── cut
│   │   ├── dbclient
│   │   ├── dirname
│   │   ├── dropbearkey
│   │   ├── du
│   │   ├── dumpimage
│   │   ├── dumpleases
│   │   ├── ecm_dump.sh
│   │   ├── env
│   │   ├── expr
│   │   ├── file
│   │   ├── find
│   │   ├── flock
│   │   ├── free
│   │   ├── ftpget
│   │   ├── ftpput
│   │   ├── funzip
│   │   ├── head
│   │   ├── hexdump
│   │   ├── hostid
│   │   ├── id
│   │   ├── ipcs
│   │   ├── iperf
│   │   ├── jshn
│   │   ├── jsonfilter
│   │   ├── killall
│   │   ├── less
│   │   ├── logger
│   │   ├── lsusb
│   │   ├── md5sum
│   │   ├── mkfifo
│   │   ├── mkimage
│   │   ├── nc
│   │   ├── ndisc6
│   │   ├── nslookup
│   │   ├── ntfs-3g
│   │   ├── ntfs-3g.probe
│   │   ├── openssl
│   │   ├── passwd
│   │   ├── perl
│   │   ├── perl5.20.2
│   │   ├── pgrep
│   │   ├── pm-is-supported
│   │   ├── printf
│   │   ├── rdisc6
│   │   ├── readlink
│   │   ├── reset
│   │   ├── resolveip
│   │   ├── rltraceroute6
│   │   ├── rngtest
│   │   ├── rrdtool
│   │   ├── rrdupdate
│   │   ├── scp
│   │   ├── seq
│   │   ├── sfe_dump
│   │   ├── signify
│   │   ├── sort
│   │   ├── sqlite3
│   │   ├── ssh
│   │   ├── strings
│   │   ├── systool
│   │   ├── tail
│   │   ├── taskset
│   │   ├── tcpsvd
│   │   ├── tcptraceroute6
│   │   ├── tee
│   │   ├── test
│   │   ├── tftp
│   │   ├── time
│   │   ├── top
│   │   ├── tr
│   │   ├── trace-cmd
│   │   ├── tracepath
│   │   ├── tracepath6
│   │   ├── traceroute
│   │   ├── traceroute6
│   │   ├── tracert6
│   │   ├── tty
│   │   ├── udhcpc6
│   │   ├── uniq
│   │   ├── unxz
│   │   ├── unzip
│   │   ├── unzipsfx
│   │   ├── uptime
│   │   ├── usign
│   │   ├── wc
│   │   ├── wget
│   │   ├── which
│   │   ├── xargs
│   │   ├── xz
│   │   ├── xzcat
│   │   ├── yes
│   │   ├── zip
│   │   ├── zipcloak
│   │   ├── zipgrep
│   │   ├── zipinfo
│   │   ├── zipnote
│   │   └── zipsplit
│   ├── lib
│   │   ├── iptables
│   │   │   ├── libip6t_DNPT.so
│   │   │   ├── libip6t_HL.so
│   │   │   ├── libip6t_NETMAP.so
│   │   │   ├── libip6t_SNPT.so
│   │   │   ├── libipt_ECN.so
│   │   │   ├── libipt_NETMAP.so
│   │   │   ├── libipt_TTL.so
│   │   │   ├── libipt_ah.so
│   │   │   ├── libxt_CLASSIFY.so
│   │   │   ├── libxt_CONNMARK.so
│   │   │   ├── libxt_DSCP.so
│   │   │   ├── libxt_IPMARK.so
│   │   │   ├── libxt_TOS.so
│   │   │   ├── libxt_addrtype.so
│   │   │   ├── libxt_connbytes.so
│   │   │   ├── libxt_connlimit.so
│   │   │   ├── libxt_ecn.so
│   │   │   ├── libxt_esp.so
│   │   │   ├── libxt_helper.so
│   │   │   ├── libxt_iface.so
│   │   │   ├── libxt_ipp2p.so
│   │   │   ├── libxt_iprange.so
│   │   │   ├── libxt_length.so
│   │   │   ├── libxt_owner.so
│   │   │   ├── libxt_physdev.so
│   │   │   ├── libxt_pkttype.so
│   │   │   ├── libxt_policy.so
│   │   │   ├── libxt_quota.so
│   │   │   ├── libxt_recent.so
│   │   │   ├── libxt_statistic.so
│   │   │   ├── libxt_string.so
│   │   │   └── libxt_tcpmss.so
│   │   ├── libart_lgpl_2.so.2
│   │   ├── libart_lgpl_2.so.2.3.21
│   │   ├── libbz2.so.1.0
│   │   ├── libbz2.so.1.0.6
│   │   ├── libcom_err.so.0
│   │   ├── libcom_err.so.0.0
│   │   ├── libconfig.so
│   │   ├── libconfig.so.9
│   │   ├── libconfig.so.9.1.3
│   │   ├── libconfuse.so.2
│   │   ├── libconfuse.so.2.0.0
│   │   ├── libcrypto.so.1.0.0
│   │   ├── libcurses.so
│   │   ├── libdaemon.so.0
│   │   ├── libdaemon.so.0.5.0
│   │   ├── libdb-4.7.so
│   │   ├── libdb-4.so
│   │   ├── libe2p.so.2
│   │   ├── libe2p.so.2.3
│   │   ├── libext2fs.so.2
│   │   ├── libext2fs.so.2.4
│   │   ├── libfal.so
│   │   ├── libffi.so.6
│   │   ├── libffi.so.6.0.1
│   │   ├── libform.so
│   │   ├── libform.so.5
│   │   ├── libform.so.5.9
│   │   ├── libfreetype.so.6
│   │   ├── libfreetype.so.6.11.4
│   │   ├── libgdbm.so.3
│   │   ├── libgdbm.so.3.0.0
│   │   ├── libhistory.so.5
│   │   ├── libhistory.so.5.2
│   │   ├── libip4tc.so
│   │   ├── libip4tc.so.0
│   │   ├── libip4tc.so.0.1.0
│   │   ├── libip6tc.so
│   │   ├── libip6tc.so.0
│   │   ├── libip6tc.so.0.1.0
│   │   ├── libiptext.so
│   │   ├── libiptext4.so
│   │   ├── libiptext6.so
│   │   ├── libjson-c.so.2
│   │   ├── libjson-c.so.2.0.1
│   │   ├── libmagic.so.1
│   │   ├── libmagic.so.1.0.0
│   │   ├── libmal.so
│   │   ├── libmal.so.3
│   │   ├── libmal.so.3.0.0
│   │   ├── libmal_uqmi.so
│   │   ├── libmal_uqmi.so.3
│   │   ├── libmal_uqmi.so.3.0.0
│   │   ├── libmal_utils.so
│   │   ├── libmal_utils.so.3
│   │   ├── libmal_utils.so.3.0.0
│   │   ├── libmenu.so
│   │   ├── libmenu.so.5
│   │   ├── libmenu.so.5.9
│   │   ├── libmnl.so.0
│   │   ├── libmnl.so.0.1.0
│   │   ├── libncurses.so
│   │   ├── libncurses.so.5
│   │   ├── libncurses.so.5.9
│   │   ├── libnetfilter_conntrack.so.3
│   │   ├── libnetfilter_conntrack.so.3.5.0
│   │   ├── libnetfilter_cthelper.so.0
│   │   ├── libnetfilter_cthelper.so.0.0.0
│   │   ├── libnetfilter_cttimeout.so.1
│   │   ├── libnetfilter_cttimeout.so.1.0.0
│   │   ├── libnetfilter_queue.so.1
│   │   ├── libnetfilter_queue.so.1.3.0
│   │   ├── libnfnetlink.so.0
│   │   ├── libnfnetlink.so.0.2.0
│   │   ├── libnl-3.so.200
│   │   ├── libnl-3.so.200.16.1
│   │   ├── libnl-genl-3.so.200
│   │   ├── libnl-genl-3.so.200.16.1
│   │   ├── libnl-nf-3.so.200
│   │   ├── libnl-nf-3.so.200.16.1
│   │   ├── libnl-route-3.so.200
│   │   ├── libnl-route-3.so.200.16.1
│   │   ├── libnl-tiny.so
│   │   ├── libntfs-3g.so.85
│   │   ├── libntfs-3g.so.85.0.0
│   │   ├── libpanel.so
│   │   ├── libpanel.so.5
│   │   ├── libpanel.so.5.9
│   │   ├── libpcap.so
│   │   ├── libpcap.so.1.3
│   │   ├── libpcap.so.1.3.0
│   │   ├── libpcre.so
│   │   ├── libpcre.so.1
│   │   ├── libpcre.so.1.2.7
│   │   ├── libpcreposix.so.0
│   │   ├── libpcreposix.so.0.0.4
│   │   ├── libpng.so.3
│   │   ├── libpng.so.3.56.0
│   │   ├── libpng12.so.0
│   │   ├── libpng12.so.0.56.0
│   │   ├── libreadline.so.5
│   │   ├── libreadline.so.5.2
│   │   ├── librrd.so.2
│   │   ├── librrd.so.2.0.15
│   │   ├── librrd_th.so.2
│   │   ├── librrd_th.so.2.0.13
│   │   ├── libsensors.so
│   │   ├── libsensors.so.4
│   │   ├── libsensors.so.4.3.2
│   │   ├── libsqlite3.so.0
│   │   ├── libsqlite3.so.0.8.6
│   │   ├── libssl.so.1.0.0
│   │   ├── libsysfs.so
│   │   ├── libsysfs.so.2
│   │   ├── libsysfs.so.2.0.1
│   │   ├── libtlvcmdrsp.so
│   │   ├── libtlvencoder.so
│   │   ├── libtlvparser.so
│   │   ├── libtlvtemplate.so
│   │   ├── libtlvutil.so
│   │   ├── libuClibc++-0.2.4.so
│   │   ├── libuClibc++.so.0
│   │   ├── libuuid.so
│   │   ├── libuuid.so.1
│   │   ├── libuuid.so.1.3.0
│   │   ├── libwlanstats.so
│   │   ├── libwnchal.so
│   │   ├── libwnchal.so.1
│   │   ├── libwnchal.so.1.0.0
│   │   ├── libxml2.so
│   │   ├── libxml2.so.2
│   │   ├── libxml2.so.2.9.2
│   │   ├── libxtables.so
│   │   ├── libxtables.so.10
│   │   ├── libxtables.so.10.0.0
│   │   ├── libz.so
│   │   ├── libz.so.1
│   │   ├── libz.so.1.2.11
│   │   ├── libzebra.so.0
│   │   ├── libzebra.so.0.0.0
│   │   ├── lowi
│   │   │   └── liblowi_client.so
│   │   ├── opkg
│   │   │   ├── info
│   │   │   │   ├── arptables.control
│   │   │   │   ├── arptables.list
│   │   │   │   ├── athdiag.control
│   │   │   │   ├── athdiag.list
│   │   │   │   ├── base-files.conffiles
│   │   │   │   ├── base-files.control
│   │   │   │   ├── base-files.list
│   │   │   │   ├── bridge.control
│   │   │   │   ├── bridge.list
│   │   │   │   ├── busybox.control
│   │   │   │   ├── busybox.list
│   │   │   │   ├── ca-certificates.control
│   │   │   │   ├── ca-certificates.list
│   │   │   │   ├── confuse.control
│   │   │   │   ├── confuse.list
│   │   │   │   ├── conntrack-tools.conffiles
│   │   │   │   ├── conntrack-tools.control
│   │   │   │   ├── conntrack-tools.list
│   │   │   │   ├── devinfo_access.control
│   │   │   │   ├── devinfo_access.list
│   │   │   │   ├── dnsmasq.conffiles
│   │   │   │   ├── dnsmasq.control
│   │   │   │   ├── dnsmasq.list
│   │   │   │   ├── dropbear.conffiles
│   │   │   │   ├── dropbear.control
│   │   │   │   ├── dropbear.list
│   │   │   │   ├── e2fsprogs.conffiles
│   │   │   │   ├── e2fsprogs.control
│   │   │   │   ├── e2fsprogs.list
│   │   │   │   ├── ethtool.control
│   │   │   │   ├── ethtool.list
│   │   │   │   ├── file.control
│   │   │   │   ├── file.list
│   │   │   │   ├── flock.control
│   │   │   │   ├── flock.list
│   │   │   │   ├── fstools.control
│   │   │   │   ├── fstools.list
│   │   │   │   ├── i2c-tools.control
│   │   │   │   ├── i2c-tools.list
│   │   │   │   ├── inadyn.control
│   │   │   │   ├── inadyn.list
│   │   │   │   ├── ip-full.conffiles
│   │   │   │   ├── ip-full.control
│   │   │   │   ├── ip-full.list
│   │   │   │   ├── ip6tables-mod-nat.control
│   │   │   │   ├── ip6tables-mod-nat.list
│   │   │   │   ├── ip6tables.control
│   │   │   │   ├── ip6tables.list
│   │   │   │   ├── iperf-mt.control
│   │   │   │   ├── iperf-mt.list
│   │   │   │   ├── iptables-mod-conntrack-extra.control
│   │   │   │   ├── iptables-mod-conntrack-extra.list
│   │   │   │   ├── iptables-mod-extra.control
│   │   │   │   ├── iptables-mod-extra.list
│   │   │   │   ├── iptables-mod-filter.control
│   │   │   │   ├── iptables-mod-filter.list
│   │   │   │   ├── iptables-mod-fullconenat.control
│   │   │   │   ├── iptables-mod-fullconenat.list
│   │   │   │   ├── iptables-mod-iface.control
│   │   │   │   ├── iptables-mod-iface.list
│   │   │   │   ├── iptables-mod-ipmark.control
│   │   │   │   ├── iptables-mod-ipmark.list
│   │   │   │   ├── iptables-mod-ipopt.control
│   │   │   │   ├── iptables-mod-ipopt.list
│   │   │   │   ├── iptables-mod-ipp2p.control
│   │   │   │   ├── iptables-mod-ipp2p.list
│   │   │   │   ├── iptables-mod-iprange.control
│   │   │   │   ├── iptables-mod-iprange.list
│   │   │   │   ├── iptables-mod-ipsec.control
│   │   │   │   ├── iptables-mod-ipsec.list
│   │   │   │   ├── iptables-mod-nat-extra.control
│   │   │   │   ├── iptables-mod-nat-extra.list
│   │   │   │   ├── iptables.control
│   │   │   │   ├── iptables.list
│   │   │   │   ├── iputils-tracepath.control
│   │   │   │   ├── iputils-tracepath.list
│   │   │   │   ├── iputils-tracepath6.control
│   │   │   │   ├── iputils-tracepath6.list
│   │   │   │   ├── jshn.control
│   │   │   │   ├── jshn.list
│   │   │   │   ├── jsonfilter.control
│   │   │   │   ├── jsonfilter.list
│   │   │   │   ├── kernel.control
│   │   │   │   ├── kernel.list
│   │   │   │   ├── kmod-8021q.control
│   │   │   │   ├── kmod-8021q.list
│   │   │   │   ├── kmod-aq_phy.control
│   │   │   │   ├── kmod-aq_phy.list
│   │   │   │   ├── kmod-arptables.control
│   │   │   │   ├── kmod-arptables.list
│   │   │   │   ├── kmod-bonding.control
│   │   │   │   ├── kmod-bonding.list
│   │   │   │   ├── kmod-bootconfig.control
│   │   │   │   ├── kmod-bootconfig.list
│   │   │   │   ├── kmod-bridge.control
│   │   │   │   ├── kmod-bridge.list
│   │   │   │   ├── kmod-button-hotplug.control
│   │   │   │   ├── kmod-button-hotplug.list
│   │   │   │   ├── kmod-crypto-aead.control
│   │   │   │   ├── kmod-crypto-aead.list
│   │   │   │   ├── kmod-crypto-aes.control
│   │   │   │   ├── kmod-crypto-aes.list
│   │   │   │   ├── kmod-crypto-arc4.control
│   │   │   │   ├── kmod-crypto-arc4.list
│   │   │   │   ├── kmod-crypto-authenc.control
│   │   │   │   ├── kmod-crypto-authenc.list
│   │   │   │   ├── kmod-crypto-cbc.control
│   │   │   │   ├── kmod-crypto-cbc.list
│   │   │   │   ├── kmod-crypto-core.control
│   │   │   │   ├── kmod-crypto-core.list
│   │   │   │   ├── kmod-crypto-crc32c.control
│   │   │   │   ├── kmod-crypto-crc32c.list
│   │   │   │   ├── kmod-crypto-deflate.control
│   │   │   │   ├── kmod-crypto-deflate.list
│   │   │   │   ├── kmod-crypto-des.control
│   │   │   │   ├── kmod-crypto-des.list
│   │   │   │   ├── kmod-crypto-ecb.control
│   │   │   │   ├── kmod-crypto-ecb.list
│   │   │   │   ├── kmod-crypto-hash.control
│   │   │   │   ├── kmod-crypto-hash.list
│   │   │   │   ├── kmod-crypto-hmac.control
│   │   │   │   ├── kmod-crypto-hmac.list
│   │   │   │   ├── kmod-crypto-iv.control
│   │   │   │   ├── kmod-crypto-iv.list
│   │   │   │   ├── kmod-crypto-manager.control
│   │   │   │   ├── kmod-crypto-manager.list
│   │   │   │   ├── kmod-crypto-md5.control
│   │   │   │   ├── kmod-crypto-md5.list
│   │   │   │   ├── kmod-crypto-ocf.control
│   │   │   │   ├── kmod-crypto-ocf.list
│   │   │   │   ├── kmod-crypto-pcompress.control
│   │   │   │   ├── kmod-crypto-pcompress.list
│   │   │   │   ├── kmod-crypto-qcrypto.control
│   │   │   │   ├── kmod-crypto-qcrypto.list
│   │   │   │   ├── kmod-crypto-rng.control
│   │   │   │   ├── kmod-crypto-rng.list
│   │   │   │   ├── kmod-crypto-sha1.control
│   │   │   │   ├── kmod-crypto-sha1.list
│   │   │   │   ├── kmod-crypto-wq.control
│   │   │   │   ├── kmod-crypto-wq.list
│   │   │   │   ├── kmod-fs-msdos.control
│   │   │   │   ├── kmod-fs-msdos.list
│   │   │   │   ├── kmod-fs-ntfs.control
│   │   │   │   ├── kmod-fs-ntfs.list
│   │   │   │   ├── kmod-fs-vfat.control
│   │   │   │   ├── kmod-fs-vfat.list
│   │   │   │   ├── kmod-fuse.control
│   │   │   │   ├── kmod-fuse.list
│   │   │   │   ├── kmod-gpio-button-hotplug.control
│   │   │   │   ├── kmod-gpio-button-hotplug.list
│   │   │   │   ├── kmod-gre.control
│   │   │   │   ├── kmod-gre.list
│   │   │   │   ├── kmod-gre6.control
│   │   │   │   ├── kmod-gre6.list
│   │   │   │   ├── kmod-hwmon-core.control
│   │   │   │   ├── kmod-hwmon-core.list
│   │   │   │   ├── kmod-hwmon-tmp102.control
│   │   │   │   ├── kmod-hwmon-tmp102.list
│   │   │   │   ├── kmod-i2c-core.control
│   │   │   │   ├── kmod-i2c-core.list
│   │   │   │   ├── kmod-input-core.control
│   │   │   │   ├── kmod-input-core.list
│   │   │   │   ├── kmod-ip6-tunnel.control
│   │   │   │   ├── kmod-ip6-tunnel.list
│   │   │   │   ├── kmod-ip6tables-extra.control
│   │   │   │   ├── kmod-ip6tables-extra.list
│   │   │   │   ├── kmod-ip6tables.control
│   │   │   │   ├── kmod-ip6tables.list
│   │   │   │   ├── kmod-ipsec.control
│   │   │   │   ├── kmod-ipsec.list
│   │   │   │   ├── kmod-ipsec4.control
│   │   │   │   ├── kmod-ipsec4.list
│   │   │   │   ├── kmod-ipsec6.control
│   │   │   │   ├── kmod-ipsec6.list
│   │   │   │   ├── kmod-ipt-compat-xtables.control
│   │   │   │   ├── kmod-ipt-compat-xtables.list
│   │   │   │   ├── kmod-ipt-conntrack-extra.control
│   │   │   │   ├── kmod-ipt-conntrack-extra.list
│   │   │   │   ├── kmod-ipt-conntrack.control
│   │   │   │   ├── kmod-ipt-conntrack.list
│   │   │   │   ├── kmod-ipt-core.control
│   │   │   │   ├── kmod-ipt-core.list
│   │   │   │   ├── kmod-ipt-ct-sctp.control
│   │   │   │   ├── kmod-ipt-ct-sctp.list
│   │   │   │   ├── kmod-ipt-extra.control
│   │   │   │   ├── kmod-ipt-extra.list
│   │   │   │   ├── kmod-ipt-filter.control
│   │   │   │   ├── kmod-ipt-filter.list
│   │   │   │   ├── kmod-ipt-fullconenat.control
│   │   │   │   ├── kmod-ipt-fullconenat.list
│   │   │   │   ├── kmod-ipt-iface.control
│   │   │   │   ├── kmod-ipt-iface.list
│   │   │   │   ├── kmod-ipt-ipmark.control
│   │   │   │   ├── kmod-ipt-ipmark.list
│   │   │   │   ├── kmod-ipt-ipopt.control
│   │   │   │   ├── kmod-ipt-ipopt.list
│   │   │   │   ├── kmod-ipt-ipp2p.control
│   │   │   │   ├── kmod-ipt-ipp2p.list
│   │   │   │   ├── kmod-ipt-iprange.control
│   │   │   │   ├── kmod-ipt-iprange.list
│   │   │   │   ├── kmod-ipt-ipsec.control
│   │   │   │   ├── kmod-ipt-ipsec.list
│   │   │   │   ├── kmod-ipt-nat-extra.control
│   │   │   │   ├── kmod-ipt-nat-extra.list
│   │   │   │   ├── kmod-ipt-nat.control
│   │   │   │   ├── kmod-ipt-nat.list
│   │   │   │   ├── kmod-ipt-nat6.control
│   │   │   │   ├── kmod-ipt-nat6.list
│   │   │   │   ├── kmod-ipt-nathelper-rtsp.control
│   │   │   │   ├── kmod-ipt-nathelper-rtsp.list
│   │   │   │   ├── kmod-iptunnel.control
│   │   │   │   ├── kmod-iptunnel.list
│   │   │   │   ├── kmod-iptunnel4.control
│   │   │   │   ├── kmod-iptunnel4.list
│   │   │   │   ├── kmod-iptunnel6.control
│   │   │   │   ├── kmod-iptunnel6.list
│   │   │   │   ├── kmod-l2tp.control
│   │   │   │   ├── kmod-l2tp.list
│   │   │   │   ├── kmod-leds-lp5562.control
│   │   │   │   ├── kmod-leds-lp5562.list
│   │   │   │   ├── kmod-ledtrig-heartbeat.control
│   │   │   │   ├── kmod-ledtrig-heartbeat.list
│   │   │   │   ├── kmod-ledtrig-timer.control
│   │   │   │   ├── kmod-ledtrig-timer.list
│   │   │   │   ├── kmod-lib-crc-ccitt.control
│   │   │   │   ├── kmod-lib-crc-ccitt.list
│   │   │   │   ├── kmod-lib-crc32c.control
│   │   │   │   ├── kmod-lib-crc32c.list
│   │   │   │   ├── kmod-lib-textsearch.control
│   │   │   │   ├── kmod-lib-textsearch.list
│   │   │   │   ├── kmod-lib-zlib.control
│   │   │   │   ├── kmod-lib-zlib.list
│   │   │   │   ├── kmod-llc.control
│   │   │   │   ├── kmod-llc.list
│   │   │   │   ├── kmod-mii.control
│   │   │   │   ├── kmod-mii.list
│   │   │   │   ├── kmod-mppe.control
│   │   │   │   ├── kmod-mppe.list
│   │   │   │   ├── kmod-nat-sctp.control
│   │   │   │   ├── kmod-nat-sctp.list
│   │   │   │   ├── kmod-nat46.control
│   │   │   │   ├── kmod-nat46.list
│   │   │   │   ├── kmod-nf-conntrack-netlink.control
│   │   │   │   ├── kmod-nf-conntrack-netlink.list
│   │   │   │   ├── kmod-nf-conntrack.control
│   │   │   │   ├── kmod-nf-conntrack.list
│   │   │   │   ├── kmod-nf-conntrack6.control
│   │   │   │   ├── kmod-nf-conntrack6.list
│   │   │   │   ├── kmod-nf-ipt.control
│   │   │   │   ├── kmod-nf-ipt.list
│   │   │   │   ├── kmod-nf-ipt6.control
│   │   │   │   ├── kmod-nf-ipt6.list
│   │   │   │   ├── kmod-nf-nat.control
│   │   │   │   ├── kmod-nf-nat.list
│   │   │   │   ├── kmod-nf-nat6.control
│   │   │   │   ├── kmod-nf-nat6.list
│   │   │   │   ├── kmod-nf-nathelper-extra.control
│   │   │   │   ├── kmod-nf-nathelper-extra.list
│   │   │   │   ├── kmod-nf-nathelper.control
│   │   │   │   ├── kmod-nf-nathelper.list
│   │   │   │   ├── kmod-nfnetlink-queue.control
│   │   │   │   ├── kmod-nfnetlink-queue.list
│   │   │   │   ├── kmod-nfnetlink.control
│   │   │   │   ├── kmod-nfnetlink.list
│   │   │   │   ├── kmod-nls-base.control
│   │   │   │   ├── kmod-nls-base.list
│   │   │   │   ├── kmod-nls-cp437.control
│   │   │   │   ├── kmod-nls-cp437.list
│   │   │   │   ├── kmod-nls-iso8859-1.control
│   │   │   │   ├── kmod-nls-iso8859-1.list
│   │   │   │   ├── kmod-ppp.control
│   │   │   │   ├── kmod-ppp.list
│   │   │   │   ├── kmod-pppoe.control
│   │   │   │   ├── kmod-pppoe.list
│   │   │   │   ├── kmod-pppol2tp.control
│   │   │   │   ├── kmod-pppol2tp.list
│   │   │   │   ├── kmod-pppox.control
│   │   │   │   ├── kmod-pppox.list
│   │   │   │   ├── kmod-pptp.control
│   │   │   │   ├── kmod-pptp.list
│   │   │   │   ├── kmod-qca-edma.control
│   │   │   │   ├── kmod-qca-edma.list
│   │   │   │   ├── kmod-qca-mcs.control
│   │   │   │   ├── kmod-qca-mcs.list
│   │   │   │   ├── kmod-qca-nss-cfi-cryptoapi.control
│   │   │   │   ├── kmod-qca-nss-cfi-cryptoapi.list
│   │   │   │   ├── kmod-qca-nss-cfi-ocf.control
│   │   │   │   ├── kmod-qca-nss-cfi-ocf.list
│   │   │   │   ├── kmod-qca-nss-crypto.control
│   │   │   │   ├── kmod-qca-nss-crypto.list
│   │   │   │   ├── kmod-qca-nss-drv-gre.control
│   │   │   │   ├── kmod-qca-nss-drv-gre.list
│   │   │   │   ├── kmod-qca-nss-drv-ipsecmgr.control
│   │   │   │   ├── kmod-qca-nss-drv-ipsecmgr.list
│   │   │   │   ├── kmod-qca-nss-drv-l2tpv2.control
│   │   │   │   ├── kmod-qca-nss-drv-l2tpv2.list
│   │   │   │   ├── kmod-qca-nss-drv-lag-mgr.control
│   │   │   │   ├── kmod-qca-nss-drv-lag-mgr.list
│   │   │   │   ├── kmod-qca-nss-drv-pptp.control
│   │   │   │   ├── kmod-qca-nss-drv-pptp.list
│   │   │   │   ├── kmod-qca-nss-drv-profile.control
│   │   │   │   ├── kmod-qca-nss-drv-profile.list
│   │   │   │   ├── kmod-qca-nss-drv-qdisc.control
│   │   │   │   ├── kmod-qca-nss-drv-qdisc.list
│   │   │   │   ├── kmod-qca-nss-drv.control
│   │   │   │   ├── kmod-qca-nss-drv.list
│   │   │   │   ├── kmod-qca-nss-ecm-premium.control
│   │   │   │   ├── kmod-qca-nss-ecm-premium.list
│   │   │   │   ├── kmod-qca-nss-gmac.control
│   │   │   │   ├── kmod-qca-nss-gmac.list
│   │   │   │   ├── kmod-qca-nss-macsec.control
│   │   │   │   ├── kmod-qca-nss-macsec.list
│   │   │   │   ├── kmod-qca-rfs.control
│   │   │   │   ├── kmod-qca-rfs.list
│   │   │   │   ├── kmod-qca-ssdk-hnat.control
│   │   │   │   ├── kmod-qca-ssdk-hnat.list
│   │   │   │   ├── kmod-qca-wifi-unified-profile.control
│   │   │   │   ├── kmod-qca-wifi-unified-profile.list
│   │   │   │   ├── kmod-qca_85xx_sw.control
│   │   │   │   ├── kmod-qca_85xx_sw.list
│   │   │   │   ├── kmod-sched-connmark.control
│   │   │   │   ├── kmod-sched-connmark.list
│   │   │   │   ├── kmod-sched-core.control
│   │   │   │   ├── kmod-sched-core.list
│   │   │   │   ├── kmod-sched.control
│   │   │   │   ├── kmod-sched.list
│   │   │   │   ├── kmod-scsi-core.control
│   │   │   │   ├── kmod-scsi-core.list
│   │   │   │   ├── kmod-shortcut-fe-cm.control
│   │   │   │   ├── kmod-shortcut-fe-cm.list
│   │   │   │   ├── kmod-shortcut-fe-drv.control
│   │   │   │   ├── kmod-shortcut-fe-drv.list
│   │   │   │   ├── kmod-shortcut-fe.control
│   │   │   │   ├── kmod-shortcut-fe.list
│   │   │   │   ├── kmod-slhc.control
│   │   │   │   ├── kmod-slhc.list
│   │   │   │   ├── kmod-stp.control
│   │   │   │   ├── kmod-stp.list
│   │   │   │   ├── kmod-udptunnel4.control
│   │   │   │   ├── kmod-udptunnel4.list
│   │   │   │   ├── kmod-udptunnel6.control
│   │   │   │   ├── kmod-udptunnel6.list
│   │   │   │   ├── libart.control
│   │   │   │   ├── libart.list
│   │   │   │   ├── libblobmsg-json.control
│   │   │   │   ├── libblobmsg-json.list
│   │   │   │   ├── libbz2.control
│   │   │   │   ├── libbz2.list
│   │   │   │   ├── libc.control
│   │   │   │   ├── libc.list
│   │   │   │   ├── libconfig.control
│   │   │   │   ├── libconfig.list
│   │   │   │   ├── libdaemon.control
│   │   │   │   ├── libdaemon.list
│   │   │   │   ├── libdb47.control
│   │   │   │   ├── libdb47.list
│   │   │   │   ├── libext2fs.control
│   │   │   │   ├── libext2fs.list
│   │   │   │   ├── libffi.control
│   │   │   │   ├── libffi.list
│   │   │   │   ├── libfreetype.control
│   │   │   │   ├── libfreetype.list
│   │   │   │   ├── libgcc.control
│   │   │   │   ├── libgcc.list
│   │   │   │   ├── libgdbm.control
│   │   │   │   ├── libgdbm.list
│   │   │   │   ├── libip4tc.control
│   │   │   │   ├── libip4tc.list
│   │   │   │   ├── libip6tc.control
│   │   │   │   ├── libip6tc.list
│   │   │   │   ├── libjson-c.control
│   │   │   │   ├── libjson-c.list
│   │   │   │   ├── libjson-script.control
│   │   │   │   ├── libjson-script.list
│   │   │   │   ├── libmagic.control
│   │   │   │   ├── libmagic.list
│   │   │   │   ├── libmnl.control
│   │   │   │   ├── libmnl.list
│   │   │   │   ├── libncurses.control
│   │   │   │   ├── libncurses.list
│   │   │   │   ├── libnetfilter-conntrack.control
│   │   │   │   ├── libnetfilter-conntrack.list
│   │   │   │   ├── libnetfilter-cthelper.control
│   │   │   │   ├── libnetfilter-cthelper.list
│   │   │   │   ├── libnetfilter-cttimeout.control
│   │   │   │   ├── libnetfilter-cttimeout.list
│   │   │   │   ├── libnetfilter-queue.control
│   │   │   │   ├── libnetfilter-queue.list
│   │   │   │   ├── libnfnetlink.control
│   │   │   │   ├── libnfnetlink.list
│   │   │   │   ├── libnl-tiny.control
│   │   │   │   ├── libnl-tiny.list
│   │   │   │   ├── libnl.control
│   │   │   │   ├── libnl.list
│   │   │   │   ├── libopenssl.control
│   │   │   │   ├── libopenssl.list
│   │   │   │   ├── libpcap.control
│   │   │   │   ├── libpcap.list
│   │   │   │   ├── libpcre.control
│   │   │   │   ├── libpcre.list
│   │   │   │   ├── libpng.control
│   │   │   │   ├── libpng.list
│   │   │   │   ├── libpthread.control
│   │   │   │   ├── libpthread.list
│   │   │   │   ├── libreadline.control
│   │   │   │   ├── libreadline.list
│   │   │   │   ├── librpc.control
│   │   │   │   ├── librpc.list
│   │   │   │   ├── librrd.control
│   │   │   │   ├── librrd.list
│   │   │   │   ├── librt.control
│   │   │   │   ├── librt.list
│   │   │   │   ├── libsensors.control
│   │   │   │   ├── libsensors.list
│   │   │   │   ├── libsqlite3.control
│   │   │   │   ├── libsqlite3.list
│   │   │   │   ├── libssp.control
│   │   │   │   ├── libssp.list
│   │   │   │   ├── libsysfs.control
│   │   │   │   ├── libsysfs.list
│   │   │   │   ├── libubox.control
│   │   │   │   ├── libubox.list
│   │   │   │   ├── libubus.control
│   │   │   │   ├── libubus.list
│   │   │   │   ├── libuci.control
│   │   │   │   ├── libuci.list
│   │   │   │   ├── libuuid.control
│   │   │   │   ├── libuuid.list
│   │   │   │   ├── libxml2.control
│   │   │   │   ├── libxml2.list
│   │   │   │   ├── libxtables.control
│   │   │   │   ├── libxtables.list
│   │   │   │   ├── lk-ipq40xx.control
│   │   │   │   ├── lk-ipq40xx.list
│   │   │   │   ├── lk-ipq806x.control
│   │   │   │   ├── lk-ipq806x.list
│   │   │   │   ├── lm-sensors-detect.control
│   │   │   │   ├── lm-sensors-detect.list
│   │   │   │   ├── lm-sensors.control
│   │   │   │   ├── lm-sensors.list
│   │   │   │   ├── logd.control
│   │   │   │   ├── logd.list
│   │   │   │   ├── lxc.control
│   │   │   │   ├── lxc.list
│   │   │   │   ├── malmanager.control
│   │   │   │   ├── malmanager.list
│   │   │   │   ├── miniupnpd.conffiles
│   │   │   │   ├── miniupnpd.control
│   │   │   │   ├── miniupnpd.list
│   │   │   │   ├── mtd.control
│   │   │   │   ├── mtd.list
│   │   │   │   ├── ndisc6.control
│   │   │   │   ├── ndisc6.list
│   │   │   │   ├── netifd.control
│   │   │   │   ├── netifd.list
│   │   │   │   ├── ntfs-3g.control
│   │   │   │   ├── ntfs-3g.list
│   │   │   │   ├── odhcp6c.control
│   │   │   │   ├── odhcp6c.list
│   │   │   │   ├── odhcpd.control
│   │   │   │   ├── odhcpd.list
│   │   │   │   ├── openssl-util.conffiles
│   │   │   │   ├── openssl-util.control
│   │   │   │   ├── openssl-util.list
│   │   │   │   ├── opkg.conffiles
│   │   │   │   ├── opkg.control
│   │   │   │   ├── opkg.list
│   │   │   │   ├── perl.control
│   │   │   │   ├── perl.list
│   │   │   │   ├── perlbase-base.control
│   │   │   │   ├── perlbase-base.list
│   │   │   │   ├── perlbase-bytes.control
│   │   │   │   ├── perlbase-bytes.list
│   │   │   │   ├── perlbase-class.control
│   │   │   │   ├── perlbase-class.list
│   │   │   │   ├── perlbase-config.control
│   │   │   │   ├── perlbase-config.list
│   │   │   │   ├── perlbase-cwd.control
│   │   │   │   ├── perlbase-cwd.list
│   │   │   │   ├── perlbase-errno.control
│   │   │   │   ├── perlbase-errno.list
│   │   │   │   ├── perlbase-essential.control
│   │   │   │   ├── perlbase-essential.list
│   │   │   │   ├── perlbase-fcntl.control
│   │   │   │   ├── perlbase-fcntl.list
│   │   │   │   ├── perlbase-file.control
│   │   │   │   ├── perlbase-file.list
│   │   │   │   ├── perlbase-filehandle.control
│   │   │   │   ├── perlbase-filehandle.list
│   │   │   │   ├── perlbase-i18n.control
│   │   │   │   ├── perlbase-i18n.list
│   │   │   │   ├── perlbase-integer.control
│   │   │   │   ├── perlbase-integer.list
│   │   │   │   ├── perlbase-io.control
│   │   │   │   ├── perlbase-io.list
│   │   │   │   ├── perlbase-list.control
│   │   │   │   ├── perlbase-list.list
│   │   │   │   ├── perlbase-locale.control
│   │   │   │   ├── perlbase-locale.list
│   │   │   │   ├── perlbase-params.control
│   │   │   │   ├── perlbase-params.list
│   │   │   │   ├── perlbase-posix.control
│   │   │   │   ├── perlbase-posix.list
│   │   │   │   ├── perlbase-re.control
│   │   │   │   ├── perlbase-re.list
│   │   │   │   ├── perlbase-scalar.control
│   │   │   │   ├── perlbase-scalar.list
│   │   │   │   ├── perlbase-selectsaver.control
│   │   │   │   ├── perlbase-selectsaver.list
│   │   │   │   ├── perlbase-socket.control
│   │   │   │   ├── perlbase-socket.list
│   │   │   │   ├── perlbase-symbol.control
│   │   │   │   ├── perlbase-symbol.list
│   │   │   │   ├── perlbase-tie.control
│   │   │   │   ├── perlbase-tie.list
│   │   │   │   ├── perlbase-utf8.control
│   │   │   │   ├── perlbase-utf8.list
│   │   │   │   ├── perlbase-xsloader.control
│   │   │   │   ├── perlbase-xsloader.list
│   │   │   │   ├── pm-utils.control
│   │   │   │   ├── pm-utils.list
│   │   │   │   ├── ppp-mod-pppoe.control
│   │   │   │   ├── ppp-mod-pppoe.list
│   │   │   │   ├── ppp-mod-pppol2tp.control
│   │   │   │   ├── ppp-mod-pppol2tp.list
│   │   │   │   ├── ppp-mod-pptp.control
│   │   │   │   ├── ppp-mod-pptp.list
│   │   │   │   ├── ppp.conffiles
│   │   │   │   ├── ppp.control
│   │   │   │   ├── ppp.list
│   │   │   │   ├── procd-nand.control
│   │   │   │   ├── procd-nand.list
│   │   │   │   ├── procd.control
│   │   │   │   ├── procd.list
│   │   │   │   ├── qca-acfg.control
│   │   │   │   ├── qca-acfg.list
│   │   │   │   ├── qca-hostap.control
│   │   │   │   ├── qca-hostap.list
│   │   │   │   ├── qca-hostapd-cli.control
│   │   │   │   ├── qca-hostapd-cli.list
│   │   │   │   ├── qca-iface-mgr-10.4.control
│   │   │   │   ├── qca-iface-mgr-10.4.list
│   │   │   │   ├── qca-lowi.control
│   │   │   │   ├── qca-lowi.list
│   │   │   │   ├── qca-spectral.control
│   │   │   │   ├── qca-spectral.list
│   │   │   │   ├── qca-ssdk-shell.control
│   │   │   │   ├── qca-ssdk-shell.list
│   │   │   │   ├── qca-thermald-10.4.control
│   │   │   │   ├── qca-thermald-10.4.list
│   │   │   │   ├── qca-wifi-fw-hw11-10.4-asic.control
│   │   │   │   ├── qca-wifi-fw-hw11-10.4-asic.list
│   │   │   │   ├── qca-wifi-fw-hw3-10.4-asic.control
│   │   │   │   ├── qca-wifi-fw-hw3-10.4-asic.list
│   │   │   │   ├── qca-wifi-fw-hw4-10.4-asic.control
│   │   │   │   ├── qca-wifi-fw-hw4-10.4-asic.list
│   │   │   │   ├── qca-wifi-fw-hw5-10.4-asic.control
│   │   │   │   ├── qca-wifi-fw-hw5-10.4-asic.list
│   │   │   │   ├── qca-wifi-fw-hw6-10.4-asic.control
│   │   │   │   ├── qca-wifi-fw-hw6-10.4-asic.list
│   │   │   │   ├── qca-wpa-cli.control
│   │   │   │   ├── qca-wpa-cli.list
│   │   │   │   ├── qca-wpa-supplicant-macsec.control
│   │   │   │   ├── qca-wpa-supplicant-macsec.list
│   │   │   │   ├── qca-wpa-supplicant.control
│   │   │   │   ├── qca-wpa-supplicant.list
│   │   │   │   ├── qcmbr-10.4.control
│   │   │   │   ├── qcmbr-10.4.list
│   │   │   │   ├── quagga-libzebra.control
│   │   │   │   ├── quagga-libzebra.list
│   │   │   │   ├── quagga-ripd.conffiles
│   │   │   │   ├── quagga-ripd.control
│   │   │   │   ├── quagga-ripd.list
│   │   │   │   ├── quagga-zebra.conffiles
│   │   │   │   ├── quagga-zebra.control
│   │   │   │   ├── quagga-zebra.list
│   │   │   │   ├── quagga.control
│   │   │   │   ├── quagga.list
│   │   │   │   ├── rdisc6.control
│   │   │   │   ├── rdisc6.list
│   │   │   │   ├── resolveip.control
│   │   │   │   ├── resolveip.list
│   │   │   │   ├── rng-tools.control
│   │   │   │   ├── rng-tools.list
│   │   │   │   ├── rrdtool.control
│   │   │   │   ├── rrdtool.list
│   │   │   │   ├── sqlite3-cli.control
│   │   │   │   ├── sqlite3-cli.list
│   │   │   │   ├── swconfig.control
│   │   │   │   ├── swconfig.list
│   │   │   │   ├── sysfsutils.control
│   │   │   │   ├── sysfsutils.list
│   │   │   │   ├── tc.control
│   │   │   │   ├── tc.list
│   │   │   │   ├── terminfo.control
│   │   │   │   ├── terminfo.list
│   │   │   │   ├── trace-cmd.control
│   │   │   │   ├── trace-cmd.list
│   │   │   │   ├── traceroute6.control
│   │   │   │   ├── traceroute6.list
│   │   │   │   ├── ubi-utils.control
│   │   │   │   ├── ubi-utils.list
│   │   │   │   ├── uboot-2016-ipq40xx.control
│   │   │   │   ├── uboot-2016-ipq40xx.list
│   │   │   │   ├── uboot-2016-ipq40xx_standard.control
│   │   │   │   ├── uboot-2016-ipq40xx_standard.list
│   │   │   │   ├── uboot-envtools.control
│   │   │   │   ├── uboot-envtools.list
│   │   │   │   ├── uboot-ipq40xx.control
│   │   │   │   ├── uboot-ipq40xx.list
│   │   │   │   ├── uboot-ipq806x-fwupgrade-tools.control
│   │   │   │   ├── uboot-ipq806x-fwupgrade-tools.list
│   │   │   │   ├── uboot-ipq806x.control
│   │   │   │   ├── uboot-ipq806x.list
│   │   │   │   ├── ubox.control
│   │   │   │   ├── ubox.list
│   │   │   │   ├── ubus.control
│   │   │   │   ├── ubus.list
│   │   │   │   ├── ubusd.control
│   │   │   │   ├── ubusd.list
│   │   │   │   ├── uci.control
│   │   │   │   ├── uci.list
│   │   │   │   ├── uclibcxx.control
│   │   │   │   ├── uclibcxx.list
│   │   │   │   ├── unzip.control
│   │   │   │   ├── unzip.list
│   │   │   │   ├── usign.control
│   │   │   │   ├── usign.list
│   │   │   │   ├── webpages.control
│   │   │   │   ├── webpages.list
│   │   │   │   ├── wireless-tools.control
│   │   │   │   ├── wireless-tools.list
│   │   │   │   ├── wnc-hal.control
│   │   │   │   ├── wnc-hal.list
│   │   │   │   ├── zip.control
│   │   │   │   ├── zip.list
│   │   │   │   ├── zlib.control
│   │   │   │   └── zlib.list
│   │   │   ├── lists
│   │   │   └── status
│   │   ├── perl5
│   │   │   └── 5.20
│   │   │       ├── CORE
│   │   │       │   └── libperl.so
│   │   │       ├── Carp
│   │   │       │   └── Heavy.pm
│   │   │       ├── Carp.pm
│   │   │       ├── Class
│   │   │       │   └── Struct.pm
│   │   │       ├── Config
│   │   │       │   ├── Extensions.pm
│   │   │       │   └── Perl
│   │   │       │       └── V.pm
│   │   │       ├── Config.pm
│   │   │       ├── Config_git.pl
│   │   │       ├── Config_heavy.pl
│   │   │       ├── Cwd.pm
│   │   │       ├── Errno.pm
│   │   │       ├── Exporter
│   │   │       │   └── Heavy.pm
│   │   │       ├── Exporter.pm
│   │   │       ├── Fcntl.pm
│   │   │       ├── File
│   │   │       │   ├── Basename.pm
│   │   │       │   ├── Compare.pm
│   │   │       │   ├── Copy.pm
│   │   │       │   ├── DosGlob.pm
│   │   │       │   ├── Fetch.pm
│   │   │       │   ├── Find.pm
│   │   │       │   ├── Glob.pm
│   │   │       │   ├── GlobMapper.pm
│   │   │       │   ├── Path.pm
│   │   │       │   ├── Spec
│   │   │       │   │   ├── Cygwin.pm
│   │   │       │   │   ├── Epoc.pm
│   │   │       │   │   ├── Functions.pm
│   │   │       │   │   ├── Mac.pm
│   │   │       │   │   ├── OS2.pm
│   │   │       │   │   ├── Unix.pm
│   │   │       │   │   ├── VMS.pm
│   │   │       │   │   └── Win32.pm
│   │   │       │   ├── Spec.pm
│   │   │       │   ├── Temp.pm
│   │   │       │   └── stat.pm
│   │   │       ├── FileHandle.pm
│   │   │       ├── I18N
│   │   │       │   ├── Collate.pm
│   │   │       │   ├── LangTags
│   │   │       │   │   ├── Detect.pm
│   │   │       │   │   └── List.pm
│   │   │       │   ├── LangTags.pm
│   │   │       │   └── Langinfo.pm
│   │   │       ├── IO
│   │   │       │   ├── Compress
│   │   │       │   │   ├── Adapter
│   │   │       │   │   │   ├── Bzip2.pm
│   │   │       │   │   │   ├── Deflate.pm
│   │   │       │   │   │   └── Identity.pm
│   │   │       │   │   ├── Base
│   │   │       │   │   │   └── Common.pm
│   │   │       │   │   ├── Base.pm
│   │   │       │   │   ├── Bzip2.pm
│   │   │       │   │   ├── Deflate.pm
│   │   │       │   │   ├── Gzip
│   │   │       │   │   │   └── Constants.pm
│   │   │       │   │   ├── Gzip.pm
│   │   │       │   │   ├── RawDeflate.pm
│   │   │       │   │   ├── Zip
│   │   │       │   │   │   └── Constants.pm
│   │   │       │   │   ├── Zip.pm
│   │   │       │   │   └── Zlib
│   │   │       │   │       ├── Constants.pm
│   │   │       │   │       └── Extra.pm
│   │   │       │   ├── Dir.pm
│   │   │       │   ├── File.pm
│   │   │       │   ├── Handle.pm
│   │   │       │   ├── Pipe.pm
│   │   │       │   ├── Poll.pm
│   │   │       │   ├── Seekable.pm
│   │   │       │   ├── Select.pm
│   │   │       │   ├── Socket
│   │   │       │   │   ├── INET.pm
│   │   │       │   │   ├── IP.pm
│   │   │       │   │   └── UNIX.pm
│   │   │       │   ├── Socket.pm
│   │   │       │   ├── Uncompress
│   │   │       │   │   ├── Adapter
│   │   │       │   │   │   ├── Bunzip2.pm
│   │   │       │   │   │   ├── Identity.pm
│   │   │       │   │   │   └── Inflate.pm
│   │   │       │   │   ├── AnyInflate.pm
│   │   │       │   │   ├── AnyUncompress.pm
│   │   │       │   │   ├── Base.pm
│   │   │       │   │   ├── Bunzip2.pm
│   │   │       │   │   ├── Gunzip.pm
│   │   │       │   │   ├── Inflate.pm
│   │   │       │   │   ├── RawInflate.pm
│   │   │       │   │   └── Unzip.pm
│   │   │       │   └── Zlib.pm
│   │   │       ├── IO.pm
│   │   │       ├── List
│   │   │       │   ├── Util
│   │   │       │   │   └── XS.pm
│   │   │       │   └── Util.pm
│   │   │       ├── Locale
│   │   │       │   ├── Codes
│   │   │       │   │   ├── Constants.pm
│   │   │       │   │   ├── Country.pm
│   │   │       │   │   ├── Country_Codes.pm
│   │   │       │   │   ├── Country_Retired.pm
│   │   │       │   │   ├── Currency.pm
│   │   │       │   │   ├── Currency_Codes.pm
│   │   │       │   │   ├── Currency_Retired.pm
│   │   │       │   │   ├── LangExt.pm
│   │   │       │   │   ├── LangExt_Codes.pm
│   │   │       │   │   ├── LangExt_Retired.pm
│   │   │       │   │   ├── LangFam.pm
│   │   │       │   │   ├── LangFam_Codes.pm
│   │   │       │   │   ├── LangFam_Retired.pm
│   │   │       │   │   ├── LangVar.pm
│   │   │       │   │   ├── LangVar_Codes.pm
│   │   │       │   │   ├── LangVar_Retired.pm
│   │   │       │   │   ├── Language.pm
│   │   │       │   │   ├── Language_Codes.pm
│   │   │       │   │   ├── Language_Retired.pm
│   │   │       │   │   ├── Script.pm
│   │   │       │   │   ├── Script_Codes.pm
│   │   │       │   │   └── Script_Retired.pm
│   │   │       │   ├── Codes.pm
│   │   │       │   ├── Country.pm
│   │   │       │   ├── Currency.pm
│   │   │       │   ├── Language.pm
│   │   │       │   ├── Maketext
│   │   │       │   │   ├── Guts.pm
│   │   │       │   │   ├── GutsLoader.pm
│   │   │       │   │   └── Simple.pm
│   │   │       │   ├── Maketext.pm
│   │   │       │   └── Script.pm
│   │   │       ├── POSIX.pm
│   │   │       ├── Params
│   │   │       │   └── Check.pm
│   │   │       ├── Scalar
│   │   │       │   └── Util.pm
│   │   │       ├── SelectSaver.pm
│   │   │       ├── Socket.pm
│   │   │       ├── Symbol.pm
│   │   │       ├── Tie
│   │   │       │   ├── Array.pm
│   │   │       │   ├── File.pm
│   │   │       │   ├── Handle.pm
│   │   │       │   ├── Hash
│   │   │       │   │   └── NamedCapture.pm
│   │   │       │   ├── Hash.pm
│   │   │       │   ├── Memoize.pm
│   │   │       │   ├── RefHash.pm
│   │   │       │   ├── Scalar.pm
│   │   │       │   ├── StdHandle.pm
│   │   │       │   └── SubstrHash.pm
│   │   │       ├── XSLoader.pm
│   │   │       ├── auto
│   │   │       │   ├── Cwd
│   │   │       │   │   └── Cwd.so
│   │   │       │   ├── Fcntl
│   │   │       │   │   └── Fcntl.so
│   │   │       │   ├── File
│   │   │       │   │   ├── DosGlob
│   │   │       │   │   │   └── DosGlob.so
│   │   │       │   │   └── Glob
│   │   │       │   │       └── Glob.so
│   │   │       │   ├── I18N
│   │   │       │   │   └── Langinfo
│   │   │       │   │       └── Langinfo.so
│   │   │       │   ├── IO
│   │   │       │   │   └── IO.so
│   │   │       │   ├── List
│   │   │       │   │   └── Util
│   │   │       │   │       └── Util.so
│   │   │       │   ├── POSIX
│   │   │       │   │   └── POSIX.so
│   │   │       │   ├── Socket
│   │   │       │   │   └── Socket.so
│   │   │       │   ├── Tie
│   │   │       │   │   └── Hash
│   │   │       │   │       └── NamedCapture
│   │   │       │   │           └── NamedCapture.so
│   │   │       │   └── re
│   │   │       │       └── re.so
│   │   │       ├── base.pm
│   │   │       ├── bytes.pm
│   │   │       ├── bytes_heavy.pl
│   │   │       ├── constant.pm
│   │   │       ├── deprecate.pm
│   │   │       ├── integer.pm
│   │   │       ├── lib.pm
│   │   │       ├── locale.pm
│   │   │       ├── overload.pm
│   │   │       ├── overloading.pm
│   │   │       ├── parent.pm
│   │   │       ├── re.pm
│   │   │       ├── strict.pm
│   │   │       ├── subs.pm
│   │   │       ├── utf8.pm
│   │   │       ├── utf8_heavy.pl
│   │   │       ├── vars.pm
│   │   │       ├── warnings
│   │   │       │   └── register.pm
│   │   │       └── warnings.pm
│   │   ├── pm-utils
│   │   │   ├── bin
│   │   │   │   ├── pm-action
│   │   │   │   └── service
│   │   │   ├── functions
│   │   │   └── pm-functions
│   │   ├── pppd
│   │   │   └── 2.4.7
│   │   │       ├── pppol2tp.so
│   │   │       ├── pptp.so
│   │   │       └── rp-pppoe.so
│   │   └── trace-cmd
│   │       └── plugins
│   │           ├── plugin_function.so
│   │           ├── plugin_hrtimer.so
│   │           ├── plugin_mac80211.so
│   │           └── plugin_sched_switch.so
│   ├── sbin
│   │   ├── 80211stats
│   │   ├── Qcmbr
│   │   ├── acfg_tool
│   │   ├── apstats
│   │   ├── arping
│   │   ├── arptables
│   │   ├── assocdenialnotify
│   │   ├── athadhoc
│   │   ├── athdiag
│   │   ├── athkey
│   │   ├── athssd
│   │   ├── athstats
│   │   ├── athstatsclr
│   │   ├── athtestcmd
│   │   ├── brctl
│   │   ├── chroot
│   │   ├── conntrack
│   │   ├── conntrackd
│   │   ├── crond
│   │   ├── devinfo_access
│   │   ├── dhcprelay
│   │   ├── dnsmasq
│   │   ├── dropbear
│   │   ├── e2fsck
│   │   ├── ethtool
│   │   ├── exttool
│   │   ├── fsck.ext2
│   │   ├── fsck.ext3
│   │   ├── fsck.ext4
│   │   ├── ftpd
│   │   ├── fw_printenv
│   │   ├── fw_setenv
│   │   ├── hostapd
│   │   ├── hostapd_cli
│   │   ├── i2cdetect
│   │   ├── i2cdump
│   │   ├── i2cget
│   │   ├── i2cset
│   │   ├── icm
│   │   ├── iface-mgr
│   │   ├── inadyn
│   │   ├── inetd
│   │   ├── insmod
│   │   ├── ip
│   │   ├── ip6tables
│   │   ├── ip6tables-restore
│   │   ├── ip6tables-save
│   │   ├── iptables
│   │   ├── iptables-restore
│   │   ├── iptables-save
│   │   ├── iwconfig
│   │   ├── iwlist
│   │   ├── iwpriv
│   │   ├── lowi-server
│   │   ├── lowi-test
│   │   ├── lsmod
│   │   ├── macsec_shell
│   │   ├── miniupnpd
│   │   ├── mke2fs
│   │   ├── mkfs.ext2
│   │   ├── mkfs.ext3
│   │   ├── mkfs.ext4
│   │   ├── modinfo
│   │   ├── modprobe
│   │   ├── ntpd
│   │   ├── ntpd-hotplug
│   │   ├── odhcp6c
│   │   ├── odhcpd
│   │   ├── odhcpd-update
│   │   ├── opkg-key
│   │   ├── pktlogconf
│   │   ├── pktlogdump
│   │   ├── pm-powersave
│   │   ├── pppd
│   │   ├── pstats
│   │   ├── quagga.init
│   │   ├── radartool
│   │   ├── ripd
│   │   ├── rmmod
│   │   ├── sensord
│   │   ├── sensors
│   │   ├── sensors-detect
│   │   ├── spectraltool
│   │   ├── speedtest-cli
│   │   ├── ssdk_sh
│   │   ├── ssidsteering
│   │   ├── tc
│   │   ├── tftpd
│   │   ├── thermald
│   │   ├── thermaltool
│   │   ├── tx99tool
│   │   ├── ubiattach
│   │   ├── ubiblock
│   │   ├── ubicrc32
│   │   ├── ubidetach
│   │   ├── ubiformat
│   │   ├── ubimkvol
│   │   ├── ubinfo
│   │   ├── ubinize
│   │   ├── ubirename
│   │   ├── ubirmvol
│   │   ├── ubirsvol
│   │   ├── ubiupdatevol
│   │   ├── udhcpd
│   │   ├── update-ca-certificates
│   │   ├── wifi_control
│   │   ├── wifi_control.idb
│   │   ├── wifi_try
│   │   ├── wifitool
│   │   ├── wlanconfig
│   │   ├── wpa_cli
│   │   ├── wpa_supplicant
│   │   ├── wps_enhc
│   │   ├── xtables-multi
│   │   └── zebra
│   └── share
│       ├── libubox
│       │   └── jshn.sh
│       ├── location
│       │   ├── lowi
│       │   └── mq
│       ├── miniupnpd
│       │   └── firewall.include
│       ├── misc
│       │   ├── magic
│       │   └── magic.mgc
│       ├── perl
│       │   └── perl-tests
│       │       └── cpan
│       │           └── Scalar-List-Utils
│       │               └── blib
│       ├── rrdtool
│       │   └── fonts
│       │       └── DejaVuSansMono-Roman.ttf
│       ├── terminfo
│       │   ├── a
│       │   │   └── ansi
│       │   ├── d
│       │   │   └── dumb
│       │   ├── l
│       │   │   └── linux
│       │   ├── r
│       │   │   ├── rxvt
│       │   │   └── rxvt-unicode
│       │   ├── s
│       │   │   └── screen
│       │   ├── v
│       │   │   ├── vt100
│       │   │   └── vt102
│       │   └── x
│       │       ├── xterm
│       │       ├── xterm-256color
│       │       └── xterm-color
│       └── udhcpc
│           └── default.script
├── var
└── www
    └── cgi-bin
        ├── gui.cgi
        └── login.cgi


</pre>
