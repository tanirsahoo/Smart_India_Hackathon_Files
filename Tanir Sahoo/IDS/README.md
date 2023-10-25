# Basic Installations code:

First we need to install Rust and Cargo in our system.
1. Code for installation: curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
2. Now set the path for Cargo:
   - echo 'export PATH=”${PATH}:~/.cargo/bin”' >> ~/.bashrc
   - export PATH="${PATH}:/root/.cargo/bin" 