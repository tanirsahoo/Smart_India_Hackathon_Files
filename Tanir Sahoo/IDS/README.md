# Basic Installation code:

First we need to install Rust and Cargo in our system.
1. Code for installation: curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
2. Now set the path for Cargo:
   - echo 'export PATH=”${PATH}:~/.cargo/bin”' >> ~/.bashrc
   - export PATH="${PATH}:/root/.cargo/bin"
3. Run the following codes as root:
   - apt-get install build-essential git libjansson-dev libpcap-dev \
                libpcre2-dev libtool libyaml-dev make pkg-config zlib1g-dev
   - apt-get install cbindgen    (OR)    cargo install --force cbindgen
4. Now run the following code:
   - apt-get install autoconf automake build-essential ccache clang curl git \
                gosu jq libbpf-dev libcap-ng0 libcap-ng-dev libelf-dev \
                libevent-dev libgeoip-dev libhiredis-dev libjansson-dev \
                liblua5.1-dev libmagic-dev libnet1-dev libpcap-dev \
                libpcre2-dev libtool libyaml-0-2 libyaml-dev m4 make \
                pkg-config python3 python3-dev python3-yaml sudo zlib1g \
                zlib1g-dev
   - cargo install --force cbindgen
5. Extra for iptables/nftables IPS integration:
   - apt-get install libnetfilter-queue-dev libnetfilter-queue1  \
                libnetfilter-log-dev libnetfilter-log1      \
                libnfnetlink-dev libnfnetlink0
6. Install Suricata: sudo apt install suricata