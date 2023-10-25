# Basic Installation code:

First we need to install Rust and Cargo in our system.
1. Code for installation: curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
2. Now set the path for Cargo:
   - echo 'export PATH=”${PATH}:~/.cargo/bin”' >> ~/.bashrc
   - export PATH="${PATH}:/root/.cargo/bin"
3. Run the following codes as root:
   - apt-get install build-essential git libjansson-dev libpcap-dev \
                libpcre2-dev libtool libyaml-dev make pkg-config zlib1g-dev