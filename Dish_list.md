Dish file list

<pre>

├── cpio-root.7z
├── cpioroot_7z
│   ├── dev
│   │   └── log
│   ├── etc
│   │   ├── cron.d
│   │   │   └── e2scrub_all
│   │   ├── dropbear
│   │   │   ├── dropbear_dss_host_key
│   │   │   ├── dropbear_ecdsa_host_key
│   │   │   ├── dropbear_ed25519_host_key
│   │   │   └── dropbear_rsa_host_key
│   │   ├── e2scrub.conf
│   │   ├── flash_info.per_box
│   │   ├── fstab
│   │   ├── group
│   │   ├── hosts
│   │   ├── init.d
│   │   │   └── ninfod.sh
│   │   ├── inputrc
│   │   ├── iproute2
│   │   │   ├── bpf_pinning
│   │   │   ├── ematch_map
│   │   │   ├── group
│   │   │   ├── nl_protos
│   │   │   ├── rt_dsfield
│   │   │   ├── rt_protos
│   │   │   ├── rt_realms
│   │   │   ├── rt_scopes
│   │   │   └── rt_tables
│   │   ├── issue
│   │   ├── linuxptp.cfg
│   │   ├── mke2fs.conf
│   │   ├── mnt_points
│   │   ├── motd
│   │   ├── mtab
│   │   ├── mtdoops-patterns
│   │   ├── network
│   │   │   ├── if-down.d
│   │   │   ├── if-post-down.d
│   │   │   ├── if-pre-up.d
│   │   │   ├── if-up.d
│   │   │   ├── interface_mappings
│   │   │   ├── interfaces
│   │   │   └── minimal_interfaces
│   │   ├── os-release
│   │   ├── passwd
│   │   ├── profile
│   │   ├── protocols
│   │   ├── resolv.conf
│   │   ├── runtime_init
│   │   ├── services
│   │   ├── shadow
│   │   ├── shells
│   │   ├── ssh
│   │   │   ├── moduli
│   │   │   ├── ssh_config
│   │   │   └── sshd_config
│   │   ├── sx-board-id
│   │   ├── sx-plat-branch
│   │   ├── sx-plat-build
│   │   ├── sx-platbundle-hash
│   │   ├── sx-plat-commit
│   │   ├── sx-rootfs-branch
│   │   ├── sx-rootfs-build
│   │   ├── sx-rootfs-commit
│   │   ├── sysconfig
│   │   │   ├── sysstat
│   │   │   └── sysstat.ioconf
│   │   ├── sysctl.conf
│   │   ├── sysctl_per_box.conf
│   │   ├── sysctl_per_vehicle.conf
│   │   └── syslog.conf
│   ├── lib
│   │   ├── ld-musl-aarch64.so.1
│   │   ├── libatomic.so.1
│   │   ├── libatomic.so.1.2.0
│   │   ├── libblkid.so.1
│   │   ├── libblkid.so.1.1.0
│   │   ├── libgcc_s.so.1
│   │   ├── libstdc++.so.6
│   │   ├── libstdc++.so.6.0.25
│   │   ├── libuuid.so.1
│   │   ├── libuuid.so.1.3.0
│   │   └── modules
│   │       └── 5.4.34-rt21-gcdddf10
│   │           ├── kernel
│   │           │   ├── fs
│   │           │   │   ├── lockd
│   │           │   │   │   └── lockd.ko
│   │           │   │   ├── nfs
│   │           │   │   │   ├── nfs.ko
│   │           │   │   │   └── nfsv3.ko
│   │           │   │   └── nfs_common
│   │           │   │       └── grace.ko
│   │           │   └── net
│   │           │       ├── bridge
│   │           │       │   └── br_netfilter.ko
│   │           │       └── sunrpc
│   │           │           └── sunrpc.ko
│   │           ├── modules.alias
│   │           ├── modules.alias.bin
│   │           ├── modules.builtin
│   │           ├── modules.builtin.alias.bin
│   │           ├── modules.builtin.bin
│   │           ├── modules.builtin.modinfo
│   │           ├── modules.dep
│   │           ├── modules.dep.bin
│   │           ├── modules.devname
│   │           ├── modules.order
│   │           ├── modules.softdep
│   │           ├── modules.symbols
│   │           └── modules.symbols.bin
│   ├── mnt
│   ├── opt
│   ├── proc
│   ├── root
│   ├── sx
│   │   ├── local
│   │   │   ├── runtime
│   │   │   └── scripts
│   │   │       └── run_scripts
│   │   │           ├── post_mount_box.sh
│   │   │           ├── pre_init_box.sh
│   │   │           ├── setup_mounts.sh
│   │   │           ├── start_box_per_board.sh
│   │   │           ├── start_box.sh
│   │   │           ├── unpack_partitions.sh
│   │   │           └── update_hosts.sh
│   │   └── proxy
│   ├── sys
│   ├── tmp
│   │   └── sa
│   ├── usr
│   │   ├── bin
│   │   │   ├── [
│   │   │   ├── [[
│   │   │   ├── adjtimex
│   │   │   ├── arch
│   │   │   ├── argon2
│   │   │   ├── arping
│   │   │   ├── ash
│   │   │   ├── ashfuncs
│   │   │   │   ├── dirs
│   │   │   │   ├── popd
│   │   │   │   └── pushd
│   │   │   ├── awk
│   │   │   ├── badblocks
│   │   │   ├── base32
│   │   │   ├── basename
│   │   │   ├── bc
│   │   │   ├── blkdeactivate
│   │   │   ├── blkdiscard
│   │   │   ├── brctl
│   │   │   ├── bridge
│   │   │   ├── bsdiff
│   │   │   ├── bspatch
│   │   │   ├── bunzip2
│   │   │   ├── busybox
│   │   │   ├── bzcat
│   │   │   ├── bzcmp
│   │   │   ├── bzdiff
│   │   │   ├── bzegrep
│   │   │   ├── bzfgrep
│   │   │   ├── bzgrep
│   │   │   ├── bzip2
│   │   │   ├── bzip2recover
│   │   │   ├── bzless
│   │   │   ├── bzmore
│   │   │   ├── cabletest
│   │   │   ├── capsh
│   │   │   ├── cat
│   │   │   ├── chattr
│   │   │   ├── check_cal.sh
│   │   │   ├── check-mtdoops
│   │   │   ├── chmod
│   │   │   ├── chown
│   │   │   ├── chroot
│   │   │   ├── chroot_untar.sh
│   │   │   ├── chrt
│   │   │   ├── cifsiostat
│   │   │   ├── cksum
│   │   │   ├── clear
│   │   │   ├── clockdiff
│   │   │   ├── cmp
│   │   │   ├── compile_et
│   │   │   ├── config-100mbps-link
│   │   │   ├── config-l3pp
│   │   │   ├── config-nxid-link
│   │   │   ├── config-peer
│   │   │   ├── config-primary
│   │   │   ├── config-tcam
│   │   │   ├── config-vlan-link
│   │   │   ├── cp
│   │   │   ├── cpio
│   │   │   ├── cryptsetup
│   │   │   ├── cryptsetup-reencrypt
│   │   │   ├── ctstat
│   │   │   ├── cut
│   │   │   ├── date
│   │   │   ├── dbclient
│   │   │   ├── dd
│   │   │   ├── ddcmon
│   │   │   ├── decode-dimms
│   │   │   ├── decode-edid
│   │   │   ├── decode-vaio
│   │   │   ├── device_tree_util.sh
│   │   │   ├── dev_init
│   │   │   ├── devlink
│   │   │   ├── devmem
│   │   │   ├── df
│   │   │   ├── diff
│   │   │   ├── dirname
│   │   │   ├── disable_pause_frames
│   │   │   ├── dlist_test
│   │   │   ├── dmesg
│   │   │   ├── dmeventd
│   │   │   ├── dmsetup
│   │   │   ├── dmstats
│   │   │   ├── dnsd
│   │   │   ├── dnsdomainname
│   │   │   ├── dropbear
│   │   │   ├── dropbearconvert
│   │   │   ├── dropbearkey
│   │   │   ├── du
│   │   │   ├── dumpe2fs
│   │   │   ├── dumpleases
│   │   │   ├── e2freefrag
│   │   │   ├── e2fsck
│   │   │   ├── e2label
│   │   │   ├── e2mmpstatus
│   │   │   ├── e2scrub
│   │   │   ├── e2scrub_all
│   │   │   ├── e2undo
│   │   │   ├── e4crypt
│   │   │   ├── ecc
│   │   │   ├── echo
│   │   │   ├── eeprog
│   │   │   ├── egrep
│   │   │   ├── enable_1pps.sh
│   │   │   ├── enable_l1l2.sh
│   │   │   ├── enable_l2_pp.sh
│   │   │   ├── env
│   │   │   ├── ethtool
│   │   │   ├── expr
│   │   │   ├── factor
│   │   │   ├── fallocate
│   │   │   ├── false
│   │   │   ├── fgrep
│   │   │   ├── filan
│   │   │   ├── filefrag
│   │   │   ├── find
│   │   │   ├── flashcp
│   │   │   ├── flash_erase
│   │   │   ├── flash_lock
│   │   │   ├── flash_unlock
│   │   │   ├── flash_utils.sh
│   │   │   ├── fold
│   │   │   ├── free
│   │   │   ├── fsck
│   │   │   ├── fsck.ext2
│   │   │   ├── fsck.ext3
│   │   │   ├── fsck.ext4
│   │   │   ├── fsfreeze
│   │   │   ├── fstrim
│   │   │   ├── fuser
│   │   │   ├── fw_printenv
│   │   │   ├── fw_setenv
│   │   │   ├── genl
│   │   │   ├── getcap
│   │   │   ├── get_device
│   │   │   ├── get_driver
│   │   │   ├── getent
│   │   │   ├── get_module
│   │   │   ├── getopt
│   │   │   ├── getpcaps
│   │   │   ├── getty
│   │   │   ├── get_vlan
│   │   │   ├── grep
│   │   │   ├── groups
│   │   │   ├── gunzip
│   │   │   ├── gzip
│   │   │   ├── head
│   │   │   ├── hexdump
│   │   │   ├── hexedit
│   │   │   ├── hostid
│   │   │   ├── hostname
│   │   │   ├── httpd
│   │   │   ├── hwclock
│   │   │   ├── hwstamp_ctl
│   │   │   ├── i2cdetect
│   │   │   ├── i2cdump
│   │   │   ├── i2cget
│   │   │   ├── i2cset
│   │   │   ├── i2c-stub-from-dump
│   │   │   ├── i2ctransfer
│   │   │   ├── id
│   │   │   ├── ifcfg
│   │   │   ├── ifconfig
│   │   │   ├── ifdown
│   │   │   ├── ifstat
│   │   │   ├── ifup
│   │   │   ├── insmod
│   │   │   ├── integritysetup
│   │   │   ├── iostat
│   │   │   ├── ip
│   │   │   ├── ip6tables
│   │   │   ├── ip6tables-apply
│   │   │   ├── ip6tables-legacy
│   │   │   ├── ip6tables-legacy-restore
│   │   │   ├── ip6tables-legacy-save
│   │   │   ├── ip6tables-restore
│   │   │   ├── ip6tables-save
│   │   │   ├── ipcrm
│   │   │   ├── ipcs
│   │   │   ├── iperf3
│   │   │   ├── ipneigh
│   │   │   ├── iptables
│   │   │   ├── iptables-apply
│   │   │   ├── iptables-legacy
│   │   │   ├── iptables-legacy-restore
│   │   │   ├── iptables-legacy-save
│   │   │   ├── iptables-restore
│   │   │   ├── iptables-save
│   │   │   ├── iptables-xml
│   │   │   ├── is_production_hardware
│   │   │   ├── kill
│   │   │   ├── killall
│   │   │   ├── killall5
│   │   │   ├── less
│   │   │   ├── link
│   │   │   ├── linux32
│   │   │   ├── linux64
│   │   │   ├── ln
│   │   │   ├── lnstat
│   │   │   ├── logger
│   │   │   ├── login
│   │   │   ├── logname
│   │   │   ├── logrotate
│   │   │   ├── logsave
│   │   │   ├── ls
│   │   │   ├── lsattr
│   │   │   ├── lsmod
│   │   │   ├── lsof
│   │   │   ├── lspci
│   │   │   ├── lsscsi
│   │   │   ├── lzcat
│   │   │   ├── lzopcat
│   │   │   ├── make_gpio_links
│   │   │   ├── make_i2c_links
│   │   │   ├── make_mtd_links
│   │   │   ├── make_partition_links
│   │   │   ├── make_pwm_links
│   │   │   ├── make_spidev_links
│   │   │   ├── make_ut_blks
│   │   │   ├── md5sum
│   │   │   ├── memtester
│   │   │   ├── microcom
│   │   │   ├── micropython
│   │   │   ├── mii-diag
│   │   │   ├── mim
│   │   │   ├── mk_cmds
│   │   │   ├── mkdir
│   │   │   ├── mkdosfs
│   │   │   ├── mke2fs
│   │   │   ├── mkfifo
│   │   │   ├── mkfs.ext2
│   │   │   ├── mkfs.ext3
│   │   │   ├── mkfs.ext4
│   │   │   ├── mklost+found
│   │   │   ├── mknod
│   │   │   ├── mkpasswd
│   │   │   ├── mktemp
│   │   │   ├── mmc
│   │   │   ├── modinfo
│   │   │   ├── more
│   │   │   ├── mount
│   │   │   ├── mount_tftp
│   │   │   ├── mpstat
│   │   │   ├── mrdated
│   │   │   ├── mtd_debug
│   │   │   ├── mtdinfo
│   │   │   ├── mtdoops
│   │   │   ├── mv
│   │   │   ├── nc
│   │   │   ├── netcat
│   │   │   ├── netstat
│   │   │   ├── nfnl_osf
│   │   │   ├── nice
│   │   │   ├── ninfod
│   │   │   ├── nl
│   │   │   ├── nohup
│   │   │   ├── nologin
│   │   │   ├── nproc
│   │   │   ├── nsenter
│   │   │   ├── nstat
│   │   │   ├── nuke
│   │   │   ├── nxid.sh
│   │   │   ├── od
│   │   │   ├── partprobe
│   │   │   ├── passwd
│   │   │   ├── paste
│   │   │   ├── patch
│   │   │   ├── pcregrep
│   │   │   ├── pcretest
│   │   │   ├── perf
│   │   │   ├── pgrep
│   │   │   ├── phc2sys
│   │   │   ├── phc_ctl
│   │   │   ├── pidof
│   │   │   ├── pidstat
│   │   │   ├── ping
│   │   │   ├── ping6
│   │   │   ├── pipe_progress
│   │   │   ├── pkill
│   │   │   ├── pmap
│   │   │   ├── pmc
│   │   │   ├── poweroff
│   │   │   ├── printenv
│   │   │   ├── printf
│   │   │   ├── procan
│   │   │   ├── ps
│   │   │   ├── pstree
│   │   │   ├── ptp4l
│   │   │   ├── pwd
│   │   │   ├── pwdx
│   │   │   ├── rdate
│   │   │   ├── rdisc
│   │   │   ├── rdma
│   │   │   ├── readlink
│   │   │   ├── readprofile
│   │   │   ├── realpath
│   │   │   ├── reboot
│   │   │   ├── rename_interfaces
│   │   │   ├── renice
│   │   │   ├── reset
│   │   │   ├── resize
│   │   │   ├── resume
│   │   │   ├── rm
│   │   │   ├── rmdir
│   │   │   ├── rngd
│   │   │   ├── rngtest
│   │   │   ├── rotate
│   │   │   ├── route
│   │   │   ├── routef
│   │   │   ├── routel
│   │   │   ├── rtacct
│   │   │   ├── rtmon
│   │   │   ├── rtpr
│   │   │   ├── rtstat
│   │   │   ├── run-init
│   │   │   ├── run-parts
│   │   │   ├── sadf
│   │   │   ├── sar
│   │   │   ├── scp
│   │   │   ├── sed
│   │   │   ├── seq
│   │   │   ├── setcap
│   │   │   ├── set_eth_prime_mac_from_ipaddr.sh
│   │   │   ├── setfattr
│   │   │   ├── setfirewall
│   │   │   ├── sethostname
│   │   │   ├── setnetwork
│   │   │   ├── setpriv
│   │   │   ├── setserial
│   │   │   ├── setsid
│   │   │   ├── setup_emmc.sh
│   │   │   ├── sftp
│   │   │   ├── sh
│   │   │   ├── sha1sum
│   │   │   ├── sha256sum
│   │   │   ├── sha3sum
│   │   │   ├── sha512sum
│   │   │   ├── shred
│   │   │   ├── sleep
│   │   │   ├── socat
│   │   │   ├── sort
│   │   │   ├── ss
│   │   │   ├── ssh
│   │   │   ├── ssh-add
│   │   │   ├── ssh-agent
│   │   │   ├── ssh-copy-id
│   │   │   ├── sshd
│   │   │   ├── ssh-keygen
│   │   │   ├── ssh-keyscan
│   │   │   ├── ssl_client
│   │   │   ├── start_console
│   │   │   ├── start_rngd
│   │   │   ├── start_ssh
│   │   │   ├── stat
│   │   │   ├── strace
│   │   │   ├── strace-log-merge
│   │   │   ├── stress
│   │   │   ├── strings
│   │   │   ├── stty
│   │   │   ├── svc
│   │   │   ├── svok
│   │   │   ├── swapoff
│   │   │   ├── swapon
│   │   │   ├── sxplatform_update
│   │   │   ├── sxruntime_kill
│   │   │   ├── sxruntime_setup
│   │   │   ├── sxruntime_start
│   │   │   ├── sxverity
│   │   │   ├── sync
│   │   │   ├── sysctl
│   │   │   ├── syslogd
│   │   │   ├── systool
│   │   │   ├── tail
│   │   │   ├── tapestat
│   │   │   ├── tar
│   │   │   ├── taskset
│   │   │   ├── tc
│   │   │   ├── tcpdump
│   │   │   ├── tee
│   │   │   ├── test
│   │   │   ├── tftp
│   │   │   ├── time
│   │   │   ├── timemaster
│   │   │   ├── timeout
│   │   │   ├── tipc
│   │   │   ├── top
│   │   │   ├── touch
│   │   │   ├── tr
│   │   │   ├── trace
│   │   │   ├── trace-cmd
│   │   │   ├── tracepath
│   │   │   ├── traceroute6
│   │   │   ├── true
│   │   │   ├── truncate
│   │   │   ├── ts
│   │   │   ├── tty
│   │   │   ├── tune2fs
│   │   │   ├── ubirename
│   │   │   ├── udhcpc
│   │   │   ├── udhcpd
│   │   │   ├── umount
│   │   │   ├── uname
│   │   │   ├── unecc
│   │   │   ├── uniq
│   │   │   ├── unlzma
│   │   │   ├── unlzop
│   │   │   ├── unpack_cal.sh
│   │   │   ├── unpack_secrets.sh
│   │   │   ├── unpack.sh
│   │   │   ├── unshare
│   │   │   ├── unxz
│   │   │   ├── unzip
│   │   │   ├── uptime
│   │   │   ├── usleep
│   │   │   ├── verify_active_proxy
│   │   │   ├── veritysetup
│   │   │   ├── version_info
│   │   │   ├── vi
│   │   │   ├── watch
│   │   │   ├── watchdog
│   │   │   ├── wc
│   │   │   ├── wget
│   │   │   ├── whatami-catson.sh
│   │   │   ├── whatami-common.sh
│   │   │   ├── whatami.sh
│   │   │   ├── which
│   │   │   ├── whoami
│   │   │   ├── xargs
│   │   │   ├── xtables-legacy-multi
│   │   │   ├── xxd
│   │   │   ├── xz
│   │   │   ├── xzcat
│   │   │   ├── yes
│   │   │   └── zcat
│   │   ├── lib
│   │   │   ├── e2fsprogs
│   │   │   │   └── e2scrub_all_cron
│   │   │   ├── libaio.so
│   │   │   ├── libaio.so.1
│   │   │   ├── libaio.so.1.0.1
│   │   │   ├── libargon2.so
│   │   │   ├── libargon2.so.1
│   │   │   ├── libblkid.so
│   │   │   ├── libbz2.so
│   │   │   ├── libbz2.so.1.0
│   │   │   ├── libbz2.so.1.0.8
│   │   │   ├── libcap.so
│   │   │   ├── libcap.so.2
│   │   │   ├── libcap.so.2.48
│   │   │   ├── libcom_err.so
│   │   │   ├── libcom_err.so.2
│   │   │   ├── libcom_err.so.2.1
│   │   │   ├── libcrypto.so
│   │   │   ├── libcryptsetup.so
│   │   │   ├── libcryptsetup.so.12
│   │   │   ├── libcryptsetup.so.12.6.0
│   │   │   ├── libc.so
│   │   │   ├── libcurses.so
│   │   │   ├── libdevmapper-event.so
│   │   │   ├── libdevmapper-event.so.1.02
│   │   │   ├── libdevmapper.so
│   │   │   ├── libdevmapper.so.1.02
│   │   │   ├── libe2p.so
│   │   │   ├── libe2p.so.2
│   │   │   ├── libe2p.so.2.3
│   │   │   ├── libevent-2.1.so.7
│   │   │   ├── libevent-2.1.so.7.0.1
│   │   │   ├── libevent_core-2.1.so.7
│   │   │   ├── libevent_core-2.1.so.7.0.1
│   │   │   ├── libevent_core.so
│   │   │   ├── libevent_extra-2.1.so.7
│   │   │   ├── libevent_extra-2.1.so.7.0.1
│   │   │   ├── libevent_extra.so
│   │   │   ├── libevent_pthreads-2.1.so.7
│   │   │   ├── libevent_pthreads-2.1.so.7.0.1
│   │   │   ├── libevent_pthreads.so
│   │   │   ├── libevent.so
│   │   │   ├── libext2fs.so
│   │   │   ├── libext2fs.so.2
│   │   │   ├── libext2fs.so.2.4
│   │   │   ├── libffi.so
│   │   │   ├── libffi.so.7
│   │   │   ├── libffi.so.7.1.0
│   │   │   ├── libform.so
│   │   │   ├── libform.so.6
│   │   │   ├── libform.so.6.1
│   │   │   ├── libgpstime.so
│   │   │   ├── libgpstime.so.0
│   │   │   ├── libi2c.so
│   │   │   ├── libi2c.so.0
│   │   │   ├── libi2c.so.0.1.1
│   │   │   ├── libip4tc.so
│   │   │   ├── libip4tc.so.2
│   │   │   ├── libip4tc.so.2.0.0
│   │   │   ├── libip6tc.so
│   │   │   ├── libip6tc.so.2
│   │   │   ├── libip6tc.so.2.0.0
│   │   │   ├── libiperf.so
│   │   │   ├── libiperf.so.0
│   │   │   ├── libiperf.so.0.0.0
│   │   │   ├── libjitterentropy.so
│   │   │   ├── libjitterentropy.so.2
│   │   │   ├── libjitterentropy.so.2.2.0
│   │   │   ├── libjson-c.so
│   │   │   ├── libjson-c.so.5
│   │   │   ├── libjson-c.so.5.1.0
│   │   │   ├── libmenu.so
│   │   │   ├── libmenu.so.6
│   │   │   ├── libmenu.so.6.1
│   │   │   ├── libmnl.so
│   │   │   ├── libmnl.so.0
│   │   │   ├── libmnl.so.0.2.0
│   │   │   ├── libncurses.so
│   │   │   ├── libncurses.so.6
│   │   │   ├── libncurses.so.6.1
│   │   │   ├── libnetfilter_queue.so
│   │   │   ├── libnetfilter_queue.so.1
│   │   │   ├── libnetfilter_queue.so.1.5.0
│   │   │   ├── libnfnetlink.so
│   │   │   ├── libnfnetlink.so.0
│   │   │   ├── libnfnetlink.so.0.2.0
│   │   │   ├── libpanel.so
│   │   │   ├── libpanel.so.6
│   │   │   ├── libpanel.so.6.1
│   │   │   ├── libpcap.so
│   │   │   ├── libpcap.so.1
│   │   │   ├── libpcap.so.1.10.0
│   │   │   ├── libpcrecpp.so
│   │   │   ├── libpcrecpp.so.0
│   │   │   ├── libpcrecpp.so.0.0.2
│   │   │   ├── libpcreposix.so
│   │   │   ├── libpcreposix.so.0
│   │   │   ├── libpcreposix.so.0.0.7
│   │   │   ├── libpcre.so
│   │   │   ├── libpcre.so.1
│   │   │   ├── libpcre.so.1.2.12
│   │   │   ├── libpopt.so
│   │   │   ├── libpopt.so.0
│   │   │   ├── libpopt.so.0.0.1
│   │   │   ├── libpsx.so
│   │   │   ├── libpsx.so.2
│   │   │   ├── libpsx.so.2.48
│   │   │   ├── libssl.so
│   │   │   ├── libss.so
│   │   │   ├── libss.so.2
│   │   │   ├── libss.so.2.0
│   │   │   ├── libsysfs.so
│   │   │   ├── libsysfs.so.2
│   │   │   ├── libsysfs.so.2.0.1
│   │   │   ├── libsyslog.so
│   │   │   ├── libsyslog.so.0
│   │   │   ├── libsyslog.so.0.0.0
│   │   │   ├── libthriftd.so
│   │   │   ├── libthriftd.so.0.13.0
│   │   │   ├── libthriftnbd.so
│   │   │   ├── libthriftnbd.so.0.13.0
│   │   │   ├── libthriftzd.so
│   │   │   ├── libthriftzd.so.0.13.0
│   │   │   ├── libuuid.so
│   │   │   ├── libxtables.so
│   │   │   ├── libxtables.so.12
│   │   │   ├── libxtables.so.12.3.0
│   │   │   ├── libz.so
│   │   │   ├── libz.so.1
│   │   │   ├── libz.so.1.2.11
│   │   │   ├── micropython
│   │   │   │   ├── abc.py
│   │   │   │   ├── argparse.py
│   │   │   │   ├── asyncio_slow.py
│   │   │   │   ├── base64.py
│   │   │   │   ├── benchmark
│   │   │   │   │   ├── boom_uasyncio.py
│   │   │   │   │   ├── test-ab-medium.sh
│   │   │   │   │   ├── test-boom-heavy.sh
│   │   │   │   │   ├── test_http_server_heavy.py
│   │   │   │   │   ├── test_http_server_light.py
│   │   │   │   │   └── test_http_server_medium.py
│   │   │   │   ├── binascii.py
│   │   │   │   ├── binhex.py
│   │   │   │   ├── bisect.py
│   │   │   │   ├── calendar.py
│   │   │   │   ├── cgi.py
│   │   │   │   ├── cmd.py
│   │   │   │   ├── codecs.py
│   │   │   │   ├── codeop.py
│   │   │   │   ├── code.py
│   │   │   │   ├── collections
│   │   │   │   │   ├── defaultdict.py
│   │   │   │   │   ├── deque.py
│   │   │   │   │   └── __init__.py
│   │   │   │   ├── concurrent
│   │   │   │   │   └── futures
│   │   │   │   │       └── __init__.py
│   │   │   │   ├── contextlib.py
│   │   │   │   ├── copy.py
│   │   │   │   ├── csv.py
│   │   │   │   ├── curses
│   │   │   │   │   └── ascii.py
│   │   │   │   ├── datetime.py
│   │   │   │   ├── dbm.py
│   │   │   │   ├── decimal.py
│   │   │   │   ├── difflib.py
│   │   │   │   ├── email
│   │   │   │   │   ├── base64mime.py
│   │   │   │   │   ├── charset.py
│   │   │   │   │   ├── _encoded_words.py
│   │   │   │   │   ├── encoders.py
│   │   │   │   │   ├── errors.py
│   │   │   │   │   ├── feedparser.py
│   │   │   │   │   ├── header.py
│   │   │   │   │   ├── iterators.py
│   │   │   │   │   ├── message.py
│   │   │   │   │   ├── _parseaddr.py
│   │   │   │   │   ├── parser.py
│   │   │   │   │   ├── _policybase.py
│   │   │   │   │   ├── quoprimime.py
│   │   │   │   │   └── utils.py
│   │   │   │   ├── errno.py
│   │   │   │   ├── example_blink.py
│   │   │   │   ├── example_call_soon.py
│   │   │   │   ├── example_chain.py
│   │   │   │   ├── example_client.py
│   │   │   │   ├── example_dirs.py
│   │   │   │   ├── example_epoll.py
│   │   │   │   ├── example-extract.py
│   │   │   │   ├── example_fork.py
│   │   │   │   ├── example_fsencode.py
│   │   │   │   ├── example_future2.py
│   │   │   │   ├── example_future.py
│   │   │   │   ├── example_getenv.py
│   │   │   │   ├── example_hello_world_bare.py
│   │   │   │   ├── example_hello_world_callback.py
│   │   │   │   ├── example_hello_world.py
│   │   │   │   ├── example_http_client.py
│   │   │   │   ├── example_http_server.py
│   │   │   │   ├── example_logging.py
│   │   │   │   ├── example_open.py
│   │   │   │   ├── example_parallel.py
│   │   │   │   ├── example_pub_button.py
│   │   │   │   ├── example_pub.py
│   │   │   │   ├── example_rw.py
│   │   │   │   ├── example_sigint_exc.py
│   │   │   │   ├── example_sigint_ign.py
│   │   │   │   ├── example_sigint.py
│   │   │   │   ├── example_strftime.py
│   │   │   │   ├── example_sub_led.py
│   │   │   │   ├── example_sub.py
│   │   │   │   ├── example_sub_robust.py
│   │   │   │   ├── example_system.py
│   │   │   │   ├── example_timer.py
│   │   │   │   ├── example_time_tuple.py
│   │   │   │   ├── example_urandom.py
│   │   │   │   ├── example_warn.py
│   │   │   │   ├── example_xively.py
│   │   │   │   ├── example_yield_coro.py
│   │   │   │   ├── fcntl.py
│   │   │   │   ├── ffilib.py
│   │   │   │   ├── fnmatch.py
│   │   │   │   ├── formatter.py
│   │   │   │   ├── fractions.py
│   │   │   │   ├── ftplib.py
│   │   │   │   ├── functools.py
│   │   │   │   ├── __future__.py
│   │   │   │   ├── getopt.py
│   │   │   │   ├── getpass.py
│   │   │   │   ├── gettext.py
│   │   │   │   ├── glob.py
│   │   │   │   ├── gzip.py
│   │   │   │   ├── hashlib
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── sha224.py
│   │   │   │   │   ├── sha256.py
│   │   │   │   │   ├── sha384.py
│   │   │   │   │   └── sha512.py
│   │   │   │   ├── heapq.py
│   │   │   │   ├── hmac.py
│   │   │   │   ├── html
│   │   │   │   │   ├── entities.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── parser.py
│   │   │   │   ├── http
│   │   │   │   │   └── client.py
│   │   │   │   ├── imaplib.py
│   │   │   │   ├── importlib.py
│   │   │   │   ├── imp.py
│   │   │   │   ├── inspect.py
│   │   │   │   ├── io.py
│   │   │   │   ├── ipaddress.py
│   │   │   │   ├── itertools.py
│   │   │   │   ├── json
│   │   │   │   │   ├── decoder.py
│   │   │   │   │   ├── encoder.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── scanner.py
│   │   │   │   │   └── tool.py
│   │   │   │   ├── keyword.py
│   │   │   │   ├── _libc.py
│   │   │   │   ├── linecache.py
│   │   │   │   ├── locale.py
│   │   │   │   ├── logging.py
│   │   │   │   ├── machine
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── pin.py
│   │   │   │   │   └── timer.py
│   │   │   │   ├── mailbox.py
│   │   │   │   ├── mailcap.py
│   │   │   │   ├── _markupbase.py
│   │   │   │   ├── mimetypes.py
│   │   │   │   ├── multiprocessing.py
│   │   │   │   ├── nntplib.py
│   │   │   │   ├── numbers.py
│   │   │   │   ├── operator.py
│   │   │   │   ├── optparse.py
│   │   │   │   ├── os
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── path.py
│   │   │   │   ├── pathlib.py
│   │   │   │   ├── pdb.py
│   │   │   │   ├── pickle.py
│   │   │   │   ├── pickletools.py
│   │   │   │   ├── pkg_resources.py
│   │   │   │   ├── pkgutil.py
│   │   │   │   ├── platform.py
│   │   │   │   ├── poplib.py
│   │   │   │   ├── posixpath.py
│   │   │   │   ├── pprint.py
│   │   │   │   ├── profile.py
│   │   │   │   ├── pty.py
│   │   │   │   ├── pwd.py
│   │   │   │   ├── pyb.py
│   │   │   │   ├── pystone_lowmem.py
│   │   │   │   ├── pystone.py
│   │   │   │   ├── queue.py
│   │   │   │   ├── quopri.py
│   │   │   │   ├── random.py
│   │   │   │   ├── readline.py
│   │   │   │   ├── reprlib.py
│   │   │   │   ├── re.py
│   │   │   │   ├── runpy.py
│   │   │   │   ├── sched.py
│   │   │   │   ├── selectors.py
│   │   │   │   ├── select.py
│   │   │   │   ├── shelve.py
│   │   │   │   ├── shlex.py
│   │   │   │   ├── shutil.py
│   │   │   │   ├── signal.py
│   │   │   │   ├── smtplib.py
│   │   │   │   ├── socket.py
│   │   │   │   ├── socketserver.py
│   │   │   │   ├── sqlite3.py
│   │   │   │   ├── ssl.py
│   │   │   │   ├── statistics.py
│   │   │   │   ├── stat.py
│   │   │   │   ├── stringprep.py
│   │   │   │   ├── string.py
│   │   │   │   ├── struct.py
│   │   │   │   ├── subprocess.py
│   │   │   │   ├── tarfile.py
│   │   │   │   ├── telnetlib.py
│   │   │   │   ├── tempfile.py
│   │   │   │   ├── test
│   │   │   │   │   ├── pystone.py
│   │   │   │   │   └── support.py
│   │   │   │   ├── tests
│   │   │   │   │   └── test.py
│   │   │   │   ├── tests.py
│   │   │   │   ├── textwrap.py
│   │   │   │   ├── threading.py
│   │   │   │   ├── timeit.py
│   │   │   │   ├── time.py
│   │   │   │   ├── traceback.py
│   │   │   │   ├── trace.py
│   │   │   │   ├── tty.py
│   │   │   │   ├── types.py
│   │   │   │   ├── typing.py
│   │   │   │   ├── uasyncio
│   │   │   │   │   ├── core.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── queues.py
│   │   │   │   ├── uasyncio.py
│   │   │   │   ├── ucontextlib.py
│   │   │   │   ├── ucurses
│   │   │   │   │   └── __init__.py
│   │   │   │   ├── umqtt
│   │   │   │   │   ├── robust.py
│   │   │   │   │   └── simple.py
│   │   │   │   ├── unicodedata.py
│   │   │   │   ├── unittest.py
│   │   │   │   ├── upip.py
│   │   │   │   ├── upip_utarfile.py
│   │   │   │   ├── upysh.py
│   │   │   │   ├── urequests.py
│   │   │   │   ├── urllib
│   │   │   │   │   ├── parse.py
│   │   │   │   │   └── urequest.py
│   │   │   │   ├── urllib.py
│   │   │   │   ├── utarfile.py
│   │   │   │   ├── uuid.py
│   │   │   │   ├── uu.py
│   │   │   │   ├── warnings.py
│   │   │   │   ├── weakref.py
│   │   │   │   ├── xmltok.py
│   │   │   │   └── zipfile.py
│   │   │   ├── os-release
│   │   │   ├── sa
│   │   │   │   ├── sa1
│   │   │   │   ├── sa2
│   │   │   │   └── sadc
│   │   │   ├── tc
│   │   │   │   ├── experimental.dist
│   │   │   │   ├── m_ipt.so
│   │   │   │   ├── m_xt.so
│   │   │   │   ├── normal.dist
│   │   │   │   ├── pareto.dist
│   │   │   │   └── paretonormal.dist
│   │   │   ├── terminfo
│   │   │   ├── traceevent
│   │   │   │   └── plugins
│   │   │   │       ├── plugin_blk.so
│   │   │   │       ├── plugin_cfg80211.so
│   │   │   │       ├── plugin_function.so
│   │   │   │       ├── plugin_futex.so
│   │   │   │       ├── plugin_hrtimer.so
│   │   │   │       ├── plugin_jbd2.so
│   │   │   │       ├── plugin_kmem.so
│   │   │   │       ├── plugin_kvm.so
│   │   │   │       ├── plugin_mac80211.so
│   │   │   │       ├── plugin_sched_switch.so
│   │   │   │       ├── plugin_scsi.so
│   │   │   │       ├── plugin_tlb.so
│   │   │   │       └── plugin_xen.so
│   │   │   └── xtables
│   │   │       ├── libip6t_ah.so
│   │   │       ├── libip6t_DNAT.so
│   │   │       ├── libip6t_DNPT.so
│   │   │       ├── libip6t_dst.so
│   │   │       ├── libip6t_eui64.so
│   │   │       ├── libip6t_frag.so
│   │   │       ├── libip6t_hbh.so
│   │   │       ├── libip6t_HL.so
│   │   │       ├── libip6t_icmp6.so
│   │   │       ├── libip6t_ipv6header.so
│   │   │       ├── libip6t_LOG.so
│   │   │       ├── libip6t_MASQUERADE.so
│   │   │       ├── libip6t_mh.so
│   │   │       ├── libip6t_NETMAP.so
│   │   │       ├── libip6t_REDIRECT.so
│   │   │       ├── libip6t_REJECT.so
│   │   │       ├── libip6t_rt.so
│   │   │       ├── libip6t_SNAT.so
│   │   │       ├── libip6t_SNPT.so
│   │   │       ├── libip6t_srh.so
│   │   │       ├── libipt_ah.so
│   │   │       ├── libipt_CLUSTERIP.so
│   │   │       ├── libipt_DNAT.so
│   │   │       ├── libipt_ECN.so
│   │   │       ├── libipt_icmp.so
│   │   │       ├── libipt_LOG.so
│   │   │       ├── libipt_MASQUERADE.so
│   │   │       ├── libipt_NETMAP.so
│   │   │       ├── libipt_realm.so
│   │   │       ├── libipt_REDIRECT.so
│   │   │       ├── libipt_REJECT.so
│   │   │       ├── libipt_SNAT.so
│   │   │       ├── libipt_TTL.so
│   │   │       ├── libipt_ULOG.so
│   │   │       ├── libxt_addrtype.so
│   │   │       ├── libxt_AUDIT.so
│   │   │       ├── libxt_bpf.so
│   │   │       ├── libxt_cgroup.so
│   │   │       ├── libxt_CHECKSUM.so
│   │   │       ├── libxt_CLASSIFY.so
│   │   │       ├── libxt_cluster.so
│   │   │       ├── libxt_comment.so
│   │   │       ├── libxt_connbytes.so
│   │   │       ├── libxt_connlimit.so
│   │   │       ├── libxt_CONNMARK.so
│   │   │       ├── libxt_CONNSECMARK.so
│   │   │       ├── libxt_conntrack.so
│   │   │       ├── libxt_cpu.so
│   │   │       ├── libxt_CT.so
│   │   │       ├── libxt_dccp.so
│   │   │       ├── libxt_devgroup.so
│   │   │       ├── libxt_DSCP.so
│   │   │       ├── libxt_ecn.so
│   │   │       ├── libxt_esp.so
│   │   │       ├── libxt_hashlimit.so
│   │   │       ├── libxt_helper.so
│   │   │       ├── libxt_HMARK.so
│   │   │       ├── libxt_IDLETIMER.so
│   │   │       ├── libxt_ipcomp.so
│   │   │       ├── libxt_iprange.so
│   │   │       ├── libxt_ipvs.so
│   │   │       ├── libxt_LED.so
│   │   │       ├── libxt_length.so
│   │   │       ├── libxt_limit.so
│   │   │       ├── libxt_mac.so
│   │   │       ├── libxt_MARK.so
│   │   │       ├── libxt_multiport.so
│   │   │       ├── libxt_nfacct.so
│   │   │       ├── libxt_NFLOG.so
│   │   │       ├── libxt_NFQUEUE.so
│   │   │       ├── libxt_NOTRACK.so
│   │   │       ├── libxt_osf.so
│   │   │       ├── libxt_owner.so
│   │   │       ├── libxt_physdev.so
│   │   │       ├── libxt_pkttype.so
│   │   │       ├── libxt_policy.so
│   │   │       ├── libxt_quota.so
│   │   │       ├── libxt_RATEEST.so
│   │   │       ├── libxt_recent.so
│   │   │       ├── libxt_rpfilter.so
│   │   │       ├── libxt_sctp.so
│   │   │       ├── libxt_SECMARK.so
│   │   │       ├── libxt_SET.so
│   │   │       ├── libxt_socket.so
│   │   │       ├── libxt_standard.so
│   │   │       ├── libxt_state.so
│   │   │       ├── libxt_statistic.so
│   │   │       ├── libxt_string.so
│   │   │       ├── libxt_SYNPROXY.so
│   │   │       ├── libxt_TCPMSS.so
│   │   │       ├── libxt_TCPOPTSTRIP.so
│   │   │       ├── libxt_tcp.so
│   │   │       ├── libxt_TEE.so
│   │   │       ├── libxt_time.so
│   │   │       ├── libxt_TOS.so
│   │   │       ├── libxt_TPROXY.so
│   │   │       ├── libxt_TRACE.so
│   │   │       ├── libxt_u32.so
│   │   │       └── libxt_udp.so
│   │   ├── lib64
│   │   ├── libexec
│   │   │   ├── perf-core
│   │   │   │   ├── perf-archive
│   │   │   │   └── perf-with-kcore
│   │   │   ├── sftp-server
│   │   │   ├── ssh-keysign
│   │   │   └── ssh-pkcs11-helper
│   │   ├── sbin
│   │   └── share
│   │       ├── et
│   │       │   ├── et_c.awk
│   │       │   └── et_h.awk
│   │       ├── ss
│   │       │   ├── ct_c.awk
│   │       │   └── ct_c.sed
│   │       ├── terminfo
│   │       │   ├── a
│   │       │   │   └── ansi
│   │       │   ├── d
│   │       │   │   └── dumb
│   │       │   ├── l
│   │       │   │   └── linux
│   │       │   ├── p
│   │       │   │   ├── putty
│   │       │   │   ├── putty-256color
│   │       │   │   └── putty-vt100
│   │       │   ├── s
│   │       │   │   ├── screen
│   │       │   │   └── screen-256color
│   │       │   ├── v
│   │       │   │   ├── vt100
│   │       │   │   ├── vt100-putty
│   │       │   │   ├── vt102
│   │       │   │   ├── vt200
│   │       │   │   └── vt220
│   │       │   └── x
│   │       │       ├── xterm
│   │       │       ├── xterm+256color
│   │       │       ├── xterm-256color
│   │       │       ├── xterm-color
│   │       │       └── xterm-xfree86
│   │       ├── udhcpc
│   │       │   ├── default.script
│   │       │   └── default.script.d
│   │       └── xtables
│   │           └── pf.os
│   └── var
│       ├── cache
│       ├── empty
│       ├── lib
│       │   ├── arpd
│       │   └── misc
│       ├── lock
│       ├── log
│       ├── run
│       ├── spool
│       ├── tmp
│       └── www
├── kernel.7z
├── kernel_7z
│   ├── kernel
│   ├── list.txt
│   ├── mmut2
│   ├── mmut4
│   ├── ramdisk
│   ├── rev1_pre_production_fdt
│   ├── rev1_production_fdt
│   ├── rev1_proto1p3_fdt
│   ├── rev1_proto2p1_fdt
│   ├── rev1_proto2p2_fdt
│   ├── rev1_proto3_fdt
│   ├── rev2_proto0_fdt
│   ├── rev2_proto1_fdt
│   ├── rev2_proto2_fdt
│   ├── rev2_proto3_fdt
│   ├── rev2_proto4_fdt
│   ├── rev3_proto0_fdt
│   ├── rev3_proto1_fdt
│   ├── utdev3
│   └── utdev4
├── KernelA.bin
├── runtime_.7z
├── runtime_7z
│   ├── bin
│   │   ├── aap_peek_poke
│   │   ├── analyze_alignment_server
│   │   ├── avs.sh
│   │   ├── connection_manager
│   │   ├── console_telemetry_relay
│   │   ├── file_edr
│   │   ├── file_to_device_mapper
│   │   ├── flash_xp70
│   │   ├── fsw_peek_poke
│   │   ├── ftrace_monitor
│   │   ├── mlog_service
│   │   ├── mount_mmc.sh
│   │   ├── mount_verity.sh
│   │   ├── phyfw
│   │   ├── phyfw_v4
│   │   ├── rx_lmac
│   │   ├── rx_lmac_v4
│   │   ├── satellite_ptp_driver
│   │   ├── scp_peek_poke
│   │   ├── setup_configs.sh
│   │   ├── setup_edr.sh
│   │   ├── setup_multicast_ut_gw.sh
│   │   ├── setup_security_packet_pipeline.sh
│   │   ├── setup_swupdate_keys.sh
│   │   ├── setup_ut.sh
│   │   ├── sta8090_driver
│   │   ├── starlink_software_update
│   │   ├── stsafe_cli
│   │   ├── system_housekeeping_monitor
│   │   ├── telemetry_funnel
│   │   ├── tx_lmac
│   │   ├── tx_lmac_v4
│   │   ├── udhcpd_start.sh
│   │   ├── umac
│   │   ├── unlock_service
│   │   ├── user_terminal_control
│   │   ├── user_terminal_frontend
│   │   ├── ut_packet_pipeline
│   │   ├── ut_packet_pipeline_privileged
│   │   ├── ut_silicon_diag
│   │   └── xp70_shiraz.srec
│   ├── dat
│   │   ├── board_rev_mmut
│   │   │   ├── aap_links
│   │   │   ├── aap_routes_to_beamformers
│   │   │   ├── aap_routes_to_catsons
│   │   │   ├── aap_tx_routing
│   │   │   ├── aip_positions_rx
│   │   │   ├── aip_positions_tx
│   │   │   ├── beamformers
│   │   │   ├── device_to_file_mapper_board_rev.include
│   │   │   ├── file_backed_devices_hardware_board_rev.include
│   │   │   ├── file_to_device_mapper
│   │   │   ├── file_to_device_mapper_to_control
│   │   │   ├── flash_hash_swupdate
│   │   │   ├── flash_update_partitions
│   │   │   ├── iio_devices
│   │   │   ├── iio_scaler
│   │   │   ├── mission.imu
│   │   │   ├── mission.tilt_axis
│   │   │   ├── rfio_mapping
│   │   │   ├── scp_mapping
│   │   │   ├── slack_dp_cals
│   │   │   ├── system_housekeeping_monitor_to_control_board_rev.include
│   │   │   ├── telemetry
│   │   │   ├── thermal_control_board_rev
│   │   │   ├── version_check
│   │   │   └── xphy_calfreq_targets_catson
│   │   ├── board_rev_rev1_pre_production
│   │   │   ├── aap_links
│   │   │   ├── aap_routes_to_beamformers
│   │   │   ├── aap_routes_to_catsons
│   │   │   ├── aap_tx_routing
│   │   │   ├── aip_positions_rx
│   │   │   ├── aip_positions_tx
│   │   │   ├── beamformers
│   │   │   ├── calibration_generic
│   │   │   │   ├── calibration_rx_ch3
│   │   │   │   ├── calibration_rx_ch4
│   │   │   │   ├── calibration_rx_ch5
│   │   │   │   ├── calibration_rx_ch6
│   │   │   │   ├── calibration_rx_ch7
│   │   │   │   ├── calibration_rx_ch8
│   │   │   │   ├── calibration_tx_ch11
│   │   │   │   ├── calibration_tx_ch12
│   │   │   │   ├── calibration_tx_ch13
│   │   │   │   ├── calibration_tx_ch14
│   │   │   │   ├── calibration_tx_ch15
│   │   │   │   ├── calibration_tx_ch16
│   │   │   │   ├── calibration_tx_ch17
│   │   │   │   └── calibration_tx_ch18
│   │   │   ├── device_to_file_mapper_board_rev.include
│   │   │   ├── file_backed_devices_hardware_board_rev.include
│   │   │   ├── file_to_device_mapper
│   │   │   ├── file_to_device_mapper_to_control
│   │   │   ├── flash_hash_swupdate
│   │   │   ├── flash_update_partitions
│   │   │   ├── iio_devices
│   │   │   ├── iio_scaler
│   │   │   ├── mission.imu
│   │   │   ├── mission.tilt_axis
│   │   │   ├── rfio_mapping
│   │   │   ├── scp_mapping
│   │   │   ├── slack_dp_cals
│   │   │   ├── system_housekeeping_monitor_to_control_board_rev.include
│   │   │   ├── telemetry
│   │   │   ├── thermal_control_board_rev
│   │   │   ├── version_check
│   │   │   └── xphy_calfreq_targets_catson
│   │   ├── board_rev_rev1_production
│   │   │   ├── aap_links
│   │   │   ├── aap_routes_to_beamformers
│   │   │   ├── aap_routes_to_catsons
│   │   │   ├── aap_tx_routing
│   │   │   ├── aip_positions_rx
│   │   │   ├── aip_positions_tx
│   │   │   ├── beamformers
│   │   │   ├── device_to_file_mapper_board_rev.include
│   │   │   ├── file_backed_devices_hardware_board_rev.include
│   │   │   ├── file_to_device_mapper
│   │   │   ├── file_to_device_mapper_to_control
│   │   │   ├── flash_hash_swupdate
│   │   │   ├── flash_update_partitions
│   │   │   ├── iio_devices
│   │   │   ├── iio_scaler
│   │   │   ├── mission.imu
│   │   │   ├── mission.tilt_axis
│   │   │   ├── rfio_mapping
│   │   │   ├── scp_mapping
│   │   │   ├── slack_dp_cals
│   │   │   ├── system_housekeeping_monitor_to_control_board_rev.include
│   │   │   ├── telemetry
│   │   │   ├── thermal_control_board_rev
│   │   │   ├── version_check
│   │   │   └── xphy_calfreq_targets_catson
│   │   ├── board_rev_rev1_proto3
│   │   │   ├── aap_links
│   │   │   ├── aap_routes_to_beamformers
│   │   │   ├── aap_routes_to_catsons
│   │   │   ├── aap_tx_routing
│   │   │   ├── aip_positions_rx
│   │   │   ├── aip_positions_tx
│   │   │   ├── beamformers
│   │   │   ├── calibration_generic
│   │   │   │   ├── calibration_rx_ch3
│   │   │   │   ├── calibration_rx_ch4
│   │   │   │   ├── calibration_rx_ch5
│   │   │   │   ├── calibration_rx_ch6
│   │   │   │   ├── calibration_rx_ch7
│   │   │   │   ├── calibration_rx_ch8
│   │   │   │   ├── calibration_tx_ch11
│   │   │   │   ├── calibration_tx_ch12
│   │   │   │   ├── calibration_tx_ch13
│   │   │   │   ├── calibration_tx_ch14
│   │   │   │   ├── calibration_tx_ch15
│   │   │   │   ├── calibration_tx_ch16
│   │   │   │   ├── calibration_tx_ch17
│   │   │   │   └── calibration_tx_ch18
│   │   │   ├── device_to_file_mapper_board_rev.include
│   │   │   ├── file_backed_devices_hardware_board_rev.include
│   │   │   ├── file_to_device_mapper
│   │   │   ├── file_to_device_mapper_to_control
│   │   │   ├── flash_hash_swupdate
│   │   │   ├── flash_update_partitions
│   │   │   ├── iio_devices
│   │   │   ├── iio_scaler
│   │   │   ├── mission.imu
│   │   │   ├── mission.tilt_axis
│   │   │   ├── rfio_mapping
│   │   │   ├── scp_mapping
│   │   │   ├── slack_dp_cals
│   │   │   ├── system_housekeeping_monitor_to_control_board_rev.include
│   │   │   ├── telemetry
│   │   │   ├── thermal_control_board_rev
│   │   │   ├── version_check
│   │   │   └── xphy_calfreq_targets_catson
│   │   ├── board_rev_rev2_proto1
│   │   │   ├── aap_links
│   │   │   ├── aap_routes_to_beamformers
│   │   │   ├── aap_routes_to_catsons
│   │   │   ├── aap_tx_routing
│   │   │   ├── aip_positions_rx
│   │   │   ├── aip_positions_tx
│   │   │   ├── beamformers
│   │   │   ├── device_to_file_mapper_board_rev.include
│   │   │   ├── file_backed_devices_hardware_board_rev.include
│   │   │   ├── file_to_device_mapper
│   │   │   ├── file_to_device_mapper_to_control
│   │   │   ├── flash_hash_swupdate
│   │   │   ├── flash_update_partitions
│   │   │   ├── iio_devices
│   │   │   ├── iio_scaler
│   │   │   ├── mission.imu
│   │   │   ├── mission.tilt_axis
│   │   │   ├── rfio_mapping
│   │   │   ├── scp_mapping
│   │   │   ├── slack_dp_cals
│   │   │   ├── system_housekeeping_monitor_to_control_board_rev.include
│   │   │   ├── telemetry
│   │   │   ├── thermal_control_board_rev
│   │   │   ├── version_check
│   │   │   └── xphy_calfreq_targets_catson
│   │   ├── board_rev_rev2_proto2
│   │   │   ├── aap_links
│   │   │   ├── aap_routes_to_beamformers
│   │   │   ├── aap_routes_to_catsons
│   │   │   ├── aap_tx_routing
│   │   │   ├── aip_positions_rx
│   │   │   ├── aip_positions_tx
│   │   │   ├── beamformers
│   │   │   ├── device_to_file_mapper_board_rev.include
│   │   │   ├── file_backed_devices_hardware_board_rev.include
│   │   │   ├── file_to_device_mapper
│   │   │   ├── file_to_device_mapper_to_control
│   │   │   ├── flash_hash_swupdate
│   │   │   ├── flash_update_partitions
│   │   │   ├── iio_devices
│   │   │   ├── iio_scaler
│   │   │   ├── mission.imu
│   │   │   ├── mission.tilt_axis
│   │   │   ├── rfio_mapping
│   │   │   ├── scp_mapping
│   │   │   ├── slack_dp_cals
│   │   │   ├── system_housekeeping_monitor_to_control_board_rev.include
│   │   │   ├── telemetry
│   │   │   ├── thermal_control_board_rev
│   │   │   ├── version_check
│   │   │   └── xphy_calfreq_targets_catson
│   │   ├── board_rev_rev2_proto3
│   │   │   ├── aap_links
│   │   │   ├── aap_routes_to_beamformers
│   │   │   ├── aap_routes_to_catsons
│   │   │   ├── aap_tx_routing
│   │   │   ├── aip_positions_rx
│   │   │   ├── aip_positions_tx
│   │   │   ├── beamformers
│   │   │   ├── device_to_file_mapper_board_rev.include
│   │   │   ├── file_backed_devices_hardware_board_rev.include
│   │   │   ├── file_to_device_mapper
│   │   │   ├── file_to_device_mapper_to_control
│   │   │   ├── flash_hash_swupdate
│   │   │   ├── flash_update_partitions
│   │   │   ├── iio_devices
│   │   │   ├── iio_scaler
│   │   │   ├── mission.imu
│   │   │   ├── mission.tilt_axis
│   │   │   ├── rfio_mapping
│   │   │   ├── scp_mapping
│   │   │   ├── slack_dp_cals
│   │   │   ├── system_housekeeping_monitor_to_control_board_rev.include
│   │   │   ├── telemetry
│   │   │   ├── thermal_control_board_rev
│   │   │   ├── version_check
│   │   │   └── xphy_calfreq_targets_catson
│   │   ├── board_rev_rev2_proto4
│   │   │   ├── aap_links
│   │   │   ├── aap_routes_to_beamformers
│   │   │   ├── aap_routes_to_catsons
│   │   │   ├── aap_tx_routing
│   │   │   ├── aip_positions_rx
│   │   │   ├── aip_positions_tx
│   │   │   ├── beamformers
│   │   │   ├── device_to_file_mapper_board_rev.include
│   │   │   ├── file_backed_devices_hardware_board_rev.include
│   │   │   ├── file_to_device_mapper
│   │   │   ├── file_to_device_mapper_to_control
│   │   │   ├── flash_hash_swupdate
│   │   │   ├── flash_update_partitions
│   │   │   ├── iio_devices
│   │   │   ├── iio_scaler
│   │   │   ├── mission.imu
│   │   │   ├── mission.tilt_axis
│   │   │   ├── rfio_mapping
│   │   │   ├── scp_mapping
│   │   │   ├── slack_dp_cals
│   │   │   ├── system_housekeeping_monitor_to_control_board_rev.include
│   │   │   ├── telemetry
│   │   │   ├── thermal_control_board_rev
│   │   │   ├── version_check
│   │   │   └── xphy_calfreq_targets_catson
│   │   ├── board_rev_rev3_proto0
│   │   │   ├── aap_links
│   │   │   ├── aap_routes_to_beamformers
│   │   │   ├── aap_routes_to_catsons
│   │   │   ├── aap_tx_routing
│   │   │   ├── aip_positions_rx
│   │   │   ├── aip_positions_tx
│   │   │   ├── beamformers
│   │   │   ├── device_to_file_mapper_board_rev.include
│   │   │   ├── file_backed_devices_hardware_board_rev.include
│   │   │   ├── file_to_device_mapper
│   │   │   ├── file_to_device_mapper_to_control
│   │   │   ├── flash_hash_swupdate
│   │   │   ├── flash_update_partitions
│   │   │   ├── iio_devices
│   │   │   ├── iio_scaler
│   │   │   ├── mission.imu
│   │   │   ├── mission.tilt_axis
│   │   │   ├── rfio_mapping
│   │   │   ├── scp_mapping
│   │   │   ├── slack_dp_cals
│   │   │   ├── system_housekeeping_monitor_to_control_board_rev.include
│   │   │   ├── telemetry
│   │   │   ├── thermal_control_board_rev
│   │   │   ├── version_check
│   │   │   └── xphy_calfreq_targets_catson
│   │   ├── board_rev_rev3_proto1
│   │   │   ├── aap_links
│   │   │   ├── aap_routes_to_beamformers
│   │   │   ├── aap_routes_to_catsons
│   │   │   ├── aap_tx_routing
│   │   │   ├── aip_positions_rx
│   │   │   ├── aip_positions_tx
│   │   │   ├── beamformers
│   │   │   ├── device_to_file_mapper_board_rev.include
│   │   │   ├── file_backed_devices_hardware_board_rev.include
│   │   │   ├── file_to_device_mapper
│   │   │   ├── file_to_device_mapper_to_control
│   │   │   ├── flash_hash_swupdate
│   │   │   ├── flash_update_partitions
│   │   │   ├── iio_devices
│   │   │   ├── iio_scaler
│   │   │   ├── mission.imu
│   │   │   ├── mission.tilt_axis
│   │   │   ├── rfio_mapping
│   │   │   ├── scp_mapping
│   │   │   ├── slack_dp_cals
│   │   │   ├── system_housekeeping_monitor_to_control_board_rev.include
│   │   │   ├── telemetry
│   │   │   ├── thermal_control_board_rev
│   │   │   ├── version_check
│   │   │   └── xphy_calfreq_targets_catson
│   │   ├── board_rev_utdev
│   │   │   ├── aap_links
│   │   │   ├── aap_routes_to_beamformers
│   │   │   ├── aap_routes_to_catsons
│   │   │   ├── aap_tx_routing
│   │   │   ├── aip_positions_rx
│   │   │   ├── aip_positions_tx
│   │   │   ├── beamformers
│   │   │   ├── device_to_file_mapper_board_rev.include
│   │   │   ├── file_backed_devices_hardware_board_rev.include
│   │   │   ├── file_to_device_mapper
│   │   │   ├── file_to_device_mapper_to_control
│   │   │   ├── flash_hash_swupdate
│   │   │   ├── flash_update_partitions
│   │   │   ├── iio_devices
│   │   │   ├── iio_scaler
│   │   │   ├── mission.imu
│   │   │   ├── mission.tilt_axis
│   │   │   ├── rfio_mapping
│   │   │   ├── scp_mapping
│   │   │   ├── slack_dp_cals
│   │   │   ├── system_housekeeping_monitor_to_control_board_rev.include
│   │   │   ├── telemetry
│   │   │   ├── thermal_control_board_rev
│   │   │   ├── version_check
│   │   │   └── xphy_calfreq_targets_catson
│   │   ├── common
│   │   │   ├── actuator_fdir
│   │   │   ├── alert_buffers
│   │   │   ├── alert_groups
│   │   │   ├── alerts
│   │   │   ├── anti_rollback
│   │   │   ├── beamformer_rollup
│   │   │   ├── ca_certs
│   │   │   ├── catson_id_user1
│   │   │   ├── catsons
│   │   │   ├── cloud_root.crt
│   │   │   ├── command_filter
│   │   │   ├── command_table
│   │   │   ├── config_model.yaml
│   │   │   ├── connection_manager_target_to_control
│   │   │   ├── connection_manager_target_to_control.j2_template
│   │   │   ├── connection_manager_to_control
│   │   │   ├── controlcode_project
│   │   │   ├── controlcode_user_repo
│   │   │   │   ├── common_sat_gw_ut
│   │   │   │   │   ├── catson_common
│   │   │   │   │   │   └── src
│   │   │   │   │   │       ├── aap_alert_template.control
│   │   │   │   │   │       ├── catson_common.project
│   │   │   │   │   │       └── catson_fuse_alerts.control
│   │   │   │   │   ├── mac_user_common
│   │   │   │   │   │   ├── src
│   │   │   │   │   │   │   ├── mac_phy_common.control
│   │   │   │   │   │   │   ├── phy_alerts_template.control
│   │   │   │   │   │   │   ├── phy_alerts_user.control
│   │   │   │   │   │   │   ├── phy_alerts_user_only.control
│   │   │   │   │   │   │   ├── phy_user.project
│   │   │   │   │   │   │   ├── rx_lmac_alerts.control
│   │   │   │   │   │   │   ├── rx_lmac_alerts_user.control
│   │   │   │   │   │   │   ├── rx_lmac_user.project
│   │   │   │   │   │   │   ├── tx_lmac_alerts.control
│   │   │   │   │   │   │   ├── tx_lmac_alerts_user.control
│   │   │   │   │   │   │   ├── tx_lmac_user.project
│   │   │   │   │   │   │   ├── umac_alerts.control
│   │   │   │   │   │   │   ├── umac_user.project
│   │   │   │   │   │   │   └── user_only.project
│   │   │   │   │   │   └── test
│   │   │   │   │   │       ├── template_test.control
│   │   │   │   │   │       └── template_test.project
│   │   │   │   │   ├── plat_common
│   │   │   │   │   │   └── src
│   │   │   │   │   │       ├── plat_common.project
│   │   │   │   │   │       └── plat_health_alerts.control
│   │   │   │   │   ├── single_string_common
│   │   │   │   │   │   └── src
│   │   │   │   │   │       ├── commanding_alerts.control
│   │   │   │   │   │       ├── file_transfer_alerts.control
│   │   │   │   │   │       ├── plat_health_alerts.control
│   │   │   │   │   │       ├── single_string_common_no_file_transfer.project
│   │   │   │   │   │       ├── single_string_common.project
│   │   │   │   │   │       └── system_performance_alerts.control
│   │   │   │   │   ├── user_common
│   │   │   │   │   │   └── src
│   │   │   │   │   │       ├── network.control
│   │   │   │   │   │       ├── throughput.control
│   │   │   │   │   │       └── user_dataplane_alerts.control
│   │   │   │   │   ├── user_common.project
│   │   │   │   │   └── util
│   │   │   │   │       └── src
│   │   │   │   │           ├── common_constants.control
│   │   │   │   │           ├── common_functions.control
│   │   │   │   │           └── util.project
│   │   │   │   └── user
│   │   │   │       ├── user
│   │   │   │       │   └── src
│   │   │   │       │       ├── eirp.control
│   │   │   │       │       ├── electrical_alerts_2dv1.control
│   │   │   │       │       ├── ftrace.control
│   │   │   │       │       ├── mesh_init.control
│   │   │   │       │       ├── monitor_connection.control
│   │   │   │       │       ├── outage_log.control
│   │   │   │       │       ├── reboot.control
│   │   │   │       │       ├── security.control
│   │   │   │       │       ├── thermal.control
│   │   │   │       │       └── user_process_alerts.control
│   │   │   │       └── user.project
│   │   │   ├── control_to_file_edr
│   │   │   ├── control_to_file_edr_per_fwd
│   │   │   ├── control_to_frontend
│   │   │   ├── control_to_payload
│   │   │   ├── control_to_phyfw
│   │   │   ├── control_to_software_update
│   │   │   ├── control_to_telemetry_funnel
│   │   │   ├── dev_ca_certs
│   │   │   ├── device_to_file_mapper
│   │   │   ├── dnsd.conf
│   │   │   ├── eirp_control
│   │   │   ├── file_backed_devices
│   │   │   ├── file_backed_devices_catson_common
│   │   │   ├── file_backed_devices_common
│   │   │   ├── file_backed_devices_common.j2_template
│   │   │   ├── file_backed_devices_hardware
│   │   │   ├── file_backed_devices.j2_template
│   │   │   ├── file_backed_devices_layer3_common
│   │   │   ├── file_edr
│   │   │   ├── file_edr_per_fwd_to_control
│   │   │   ├── file_edr_per_tape_to_control
│   │   │   ├── file_to_device_mapper_to_control_v1.include
│   │   │   ├── file_to_device_mapper_to_control_v2.include
│   │   │   ├── file_to_device_mapper_to_control_v3.include
│   │   │   ├── file_to_device_mapper_v1.include
│   │   │   ├── file_to_device_mapper_v2.include
│   │   │   ├── file_to_device_mapper_v3.include
│   │   │   ├── flash_hash_to_control
│   │   │   ├── flash_hash_to_control_catson_ab_include
│   │   │   ├── flash_partitions_to_hash_catson_ab
│   │   │   ├── frontend_to_control
│   │   │   ├── ft_sync
│   │   │   ├── gnc_mode_idle
│   │   │   ├── hacky_cdma_plan_v1
│   │   │   ├── hacky_cdma_plan_v2
│   │   │   ├── hacky_cdma_plan_v3
│   │   │   ├── housekeeping.j2_macro
│   │   │   ├── httpd.conf
│   │   │   ├── iio_scaler_v1.include
│   │   │   ├── iio_scaler_v2.include
│   │   │   ├── iio_scaler_v3.include
│   │   │   ├── init.state
│   │   │   ├── l1sync_links_catson
│   │   │   ├── lmac_rx_extra_to_control
│   │   │   ├── lmac_rx_to_control
│   │   │   ├── lmac_tx_extra_to_control
│   │   │   ├── lmac_tx_to_control
│   │   │   ├── manual.state
│   │   │   ├── mesh
│   │   │   ├── mission.actuator_control
│   │   │   ├── mission.all
│   │   │   ├── mission.attitude_determination
│   │   │   ├── mission.ekf
│   │   │   ├── mission.gnc_alarms
│   │   │   ├── mission_gnc_components
│   │   │   ├── mission_gnc_controller
│   │   │   ├── mission.navigation
│   │   │   ├── mission.reliability_metrics
│   │   │   ├── mpi_table.bin
│   │   │   ├── node_directory
│   │   │   ├── node_directory_common_sat_gw_ut.include
│   │   │   ├── node_mgr_user1
│   │   │   ├── obstruction_map
│   │   │   ├── obstruction_predictor
│   │   │   ├── phi_theta_eirp_scaling_lut
│   │   │   ├── phy_fsw_burst_det_info_to_control
│   │   │   ├── phy_fsw_ranging_info_to_control
│   │   │   ├── phy_rx_extra_to_control
│   │   │   ├── phy_rx_high_rate_to_control
│   │   │   ├── phy_rx_to_control
│   │   │   ├── phy_tx_to_control
│   │   │   ├── platform_alerts_bus.raven
│   │   │   ├── post_pcba_rules_common
│   │   │   ├── post_pcba_rules_v1
│   │   │   ├── post_pcba_rules_v2
│   │   │   ├── post_pcba_rules_v3
│   │   │   ├── pps_time
│   │   │   ├── ptp4l.cfg
│   │   │   ├── rds_rollup
│   │   │   ├── reboot_control
│   │   │   ├── rules.json
│   │   │   ├── runtime
│   │   │   ├── runtime.j2_template
│   │   │   ├── runtime_priorities
│   │   │   ├── satellite_ptp_driver_to_control
│   │   │   ├── service_directory
│   │   │   ├── service_directory_common_sat_gw_ut.include
│   │   │   ├── slope_channels
│   │   │   ├── software_update_to_control
│   │   │   ├── sr_interface_manager
│   │   │   ├── sr_runtime_to_control
│   │   │   ├── sta8090_to_control
│   │   │   ├── state_registry_variables
│   │   │   ├── static_keys.json
│   │   │   ├── swupdate_dev_pubkey
│   │   │   ├── swupdate_release_pubkey
│   │   │   ├── system_housekeeping_monitor_to_control
│   │   │   ├── system_housekeeping_monitor_to_control_catson_common.include
│   │   │   ├── system_housekeeping_monitor_to_control_common.include
│   │   │   ├── system_housekeeping_monitor_to_control_common.include.j2_template
│   │   │   ├── telemetry_50hz.include
│   │   │   ├── telemetry_adc_v1.include
│   │   │   ├── telemetry_adc_v2.include
│   │   │   ├── telemetry_adc_v3.include
│   │   │   ├── telemetry_always_on.include
│   │   │   ├── telemetry_connection_manager.include
│   │   │   ├── telemetry_console
│   │   │   ├── telemetry_file_edr
│   │   │   ├── telemetry_fsw.include
│   │   │   ├── telemetry_ftrace
│   │   │   ├── telemetry_funnel_to_control
│   │   │   ├── telemetry_gnc.include
│   │   │   ├── telemetry_gps_driver
│   │   │   ├── telemetry_housekeeping
│   │   │   ├── telemetry_housekeeping_catson_common.include
│   │   │   ├── telemetry_housekeeping_catson_common.include.j2_template
│   │   │   ├── telemetry_housekeeping_common.include
│   │   │   ├── telemetry_housekeeping_common.include.j2_template
│   │   │   ├── telemetry_housekeeping_debug.include
│   │   │   ├── telemetry_housekeeping.j2_template
│   │   │   ├── telemetry_housekeeping_version_info.j2_macro
│   │   │   ├── telemetry.j2_macro
│   │   │   ├── telemetry_lmac_rx.include
│   │   │   ├── telemetry_lmac_tx.include
│   │   │   ├── telemetry_mac_logging
│   │   │   ├── telemetry_packet_pipeline.include
│   │   │   ├── telemetry_phy_rx.include
│   │   │   ├── telemetry_phy_tx.include
│   │   │   ├── telemetry_ptp_driver
│   │   │   ├── telemetry_satellite_ptp_driver.include
│   │   │   ├── telemetry_shiraz_factory_v1.include
│   │   │   ├── telemetry_shiraz_factory_v1.include.j2_template
│   │   │   ├── telemetry_shiraz_factory_v2.include
│   │   │   ├── telemetry_shiraz_factory_v2.include.j2_template
│   │   │   ├── telemetry_shiraz_factory_v3.include
│   │   │   ├── telemetry_shiraz_factory_v3.include.j2_template
│   │   │   ├── telemetry_shiraz_v1.include
│   │   │   ├── telemetry_shiraz_v1.include.j2_template
│   │   │   ├── telemetry_shiraz_v2.include
│   │   │   ├── telemetry_shiraz_v2.include.j2_template
│   │   │   ├── telemetry_shiraz_v3.include
│   │   │   ├── telemetry_shiraz_v3.include.j2_template
│   │   │   ├── telemetry_software_update
│   │   │   ├── telemetry_sta8090.include
│   │   │   ├── telemetry_umac.include
│   │   │   ├── telemetry_ut_factory.include
│   │   │   ├── telemetry_ut_factory_v1.include
│   │   │   ├── telemetry_ut_factory_v3.include
│   │   │   ├── template_eyescan
│   │   │   ├── template_mtdoops
│   │   │   ├── template_phc2sys
│   │   │   ├── template_proc_buddyinfo
│   │   │   ├── template_proc_meminfo
│   │   │   ├── template_proc_net_netstat
│   │   │   ├── template_proc_net_snmp
│   │   │   ├── template_proc_net_sockstat
│   │   │   ├── template_proc_net_softnet_stat
│   │   │   ├── template_proc_pid_stat
│   │   │   ├── template_proc_pid_status
│   │   │   ├── template_proc_stat
│   │   │   ├── template_proc_sys_fs_file_nr
│   │   │   ├── template_proc_tty_driver_st_asc
│   │   │   ├── template_proc_uptime
│   │   │   ├── template_ptp4l
│   │   │   ├── template_pushpull_timing
│   │   │   ├── template_runtime_stats
│   │   │   ├── template_tc_class_htb_statistics
│   │   │   ├── text_patterns
│   │   │   ├── thermal_control
│   │   │   ├── tunnel_ca_dev.pem
│   │   │   ├── tunnel_ca_prod.pem
│   │   │   ├── udhcpd.conf
│   │   │   ├── umac_to_control
│   │   │   ├── unlock_verification_dev_key
│   │   │   ├── unlock_verification_key
│   │   │   ├── update_endpoints
│   │   │   ├── user.master
│   │   │   ├── ut_packet_pipeline_to_control
│   │   │   └── xphy_calfreq_targets_dbf
│   │   ├── connection_manager
│   │   │   ├── system_configuration.json
│   │   │   └── ut_cm_configuration.json
│   │   ├── dev
│   │   │   └── hq
│   │   │       ├── board_rev_mmut
│   │   │       ├── board_rev_rev1_pre_production
│   │   │       ├── board_rev_rev1_production
│   │   │       ├── board_rev_rev1_proto3
│   │   │       ├── board_rev_rev2_proto1
│   │   │       ├── board_rev_rev2_proto2
│   │   │       ├── board_rev_rev2_proto3
│   │   │       ├── board_rev_rev2_proto4
│   │   │       ├── board_rev_rev3_proto0
│   │   │       ├── board_rev_rev3_proto1
│   │   │       ├── board_rev_utdev
│   │   │       ├── connection_manager
│   │   │       ├── fused_state_dev
│   │   │       ├── fused_state_prod
│   │   │       ├── user
│   │   │       │   └── target
│   │   │       └── www
│   │   ├── fused_state_dev
│   │   │   ├── init.event
│   │   │   └── multicast_interfaces
│   │   ├── fused_state_prod
│   │   │   ├── init.event
│   │   │   └── multicast_interfaces
│   │   └── www
│   │       ├── api.bundle.web.js.gz
│   │       ├── app.bundle.web.js.gz
│   │       ├── emc-test.html
│   │       ├── emc-test.js
│   │       ├── icon.png
│   │       ├── index.html
│   │       ├── manifest.json
│   │       ├── regulatory-label
│   │       ├── regulatory-label.png
│   │       └── starlink-logo-white.png
│   └── revision_info
│       └── version_info.txt
└── runtime.tar.lz
</pre>
