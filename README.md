## Installation

```bash
python3 -m pip install -r requirements.txt

# or

pip3 install -r requirements.txt
```

Requires Python 3.8 or higher.

## Usage

```bash
$ python main.py

Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  search-pubkey  Search Solana vanity pubkey
  show-device    Show OpenCL devices
```

### Search Pubkey

```bash
$ python main.py search-pubkey --help

Usage: main.py search-pubkey [OPTIONS]

  Search Solana vanity pubkey

Options:
  --starts-with TEXT              Public key starts with the indicated prefix.
  --ends-with TEXT                Public key ends with the indicated suffix.
  --count INTEGER                 Count of pubkeys to generate.  [default: 1]
  --output-dir DIRECTORY          Output directory.  [default: ./]
  --select-device / --no-select-device
                                  Select OpenCL device manually  [default: no-
                                  select-device]
  --iteration-bits INTEGER        Number of the iteration occupied bits.
                                  Recommended 24, 26, 28, 30, 32. The larger
                                  the bits, the longer it takes to complete an
                                  iteration.  [default: 24]
  --help                          Show this message and exit.
```

Example:

```bash
$ python main.py search-pubkey --starts-with SoL

[INFO 2024-05-11 03:17:57,110] Searching Solana pubkey that starts with 'SoL' and ends with ''
[INFO 2024-05-11 03:17:57,161] Searching with 1 OpenCL devices
[INFO 2024-05-11 03:18:06,034] Speed: 1.89 MH/s
[INFO 2024-05-11 03:18:06,036] Found: SoLJqsivM2R8Y2GXhfvKJoFM1aDAsmwMBLbbFwAZWR1
```

Verify Keypairs file via Solana CLI:

```bash
$ solana-keygen pubkey SoLJqsivM2R8Y2GXhfvKJoFM1aDAsmwMBLbbFwAZWR1.json

SoLJqsivM2R8Y2GXhfvKJoFM1aDAsmwMBLbbFwAZWR1
```
