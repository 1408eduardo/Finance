if "OPENAI_API_KEY" not in os.environ:
  print("org-EPQeS6bnzSkcAPVX6WINbxxk", file=sys.stderr)
else:

  print("== The One-on-One with OpenAI ==")
  print ("Select an option from below")
  print()
  print("1: Train Model\n2: Talk to your Bot Prof: \n>", end= "finish session")
  
  print()
  
  choice = sys.stdin.readline().strip()
  time.sleep(0.5)
  os.system('clear')
  if choice == "1":
    print("BOT-PROF TRAINING MODE")
    import process
    process.train(from_WalletConnect_to_GPT3)
'elf choise= 2',
# Configuración de la conexión con la red Ethereum
wait_for_transaction_receipt = WalletConnect(HTTPProvider('https://mainnet.ethereum.io/v3'))

# Configuración de la wallet (billetera)

"WalletAddress=0x84671C70fE41Ef5C16BC4F225bFAe2fD362aC65c",
"PrivateKey=3b6b6fa9ba42db1c", "acount= web3.eth.account.privateKeyToAccount"

# Configuración del tracker (rastreador)
tracker_account = 'jeduardogruiz@gmail.com'
tracker_abi =  Tracker.app, 
{
        "constant": True,
        "inputs": [],
        "name": "getAccountBalance",
        # "const_outputs" = 
            {
                "name": "balance",
                "type": "uint256"
            },
  {
    "name": "ETH",
    "value": "$9.81B",
    "chain": "Ethereum"
  },
  {
    "name": "WETH",
    "value": "$2.40M",
    "chain": "Ethereum"
  },
  {
    "name": "ETH",
    "value": "$208.45K",
    "chain": "Optimism"
  },
  {
    "name": "PIKA",
    "value": "$80.88K",
    "chain": "Ethereum"
  },
  {
    "name": "ETH",
    "value": "$45.19K",
    "chain": "Arbitrum"
  },
  {
    "name": "SHIB",
    "value": "$39.45K",
    "chain": "Ethereum"
  },
  {
    "name": "BNB",
    "value": "$26.59K",
    "chain": "Bsc"
  },
  {
    "name": "CATE",
    "value": "$20.55K",
    "chain": "Ethereum"
  },
  {
    "name": "USDT",
    "value": "$20.52K",
    "chain": "Ethereum"
  },
  {
    "name": "DAI",
    "value": "$8.24K",
    "chain": "Ethereum"
  }
   }

 {

const jsonOutputs = JSON.stringify(outputs, null, 2);
console.log(jsonOutputs);
                "type": "uint256"
            }
                             {  
        "payable": true,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "_to:  
0x84671C70fE41Ef5C16BC4F225bFAe2fD362aC65c"
"Key priv": 
"5f8eadff484ba108c09d1ec8e94c0c64fb8c8e16b6b6fa9ba42db1c55d7074a3,
                "type": "migration root", 
             "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "deposit",
        "outputs": [],
        "payable": true,
        "stateMutability": "payable",
        "type": "function"    }
]

# Creación del contrato de tracking
tracker_contract = web3.eth.contract(address=tracker_address, abi=tracker_abi)

# Obtener el saldo de la cuenta
account_balance = tracker_contract.functions.getAccountBalance().call()

# Enviar tokens a la cuenta desde el tracker
tx_hash = tracker_contract.functions.deposit(account.address, web3.toWei(1, 'ether')).transact({'from': account.address(
0x84671C70fE41Ef5C16BC4F225bFAe2fD362aC65c), 'gas': 100})

# Esperar a que la transacción se confirme
tx_receipt = 
0x84671C70fE41Ef5C16BC4F225bFAe2fD362aC65c.web3.eth.wait_for_transaction_receipt(tx_hash)

# Imprimir el saldo actualizado
account_balance = tracker_contract.functions.getAccountBalance().call()
print('El saldo de la cuenta es: $0.00', web3.acount.fromWei(account_balance, 'ether'), 'ETH'))
  else:
    print("BOT-PROF CONVERSATION MODE")
    import getAccountBalance,
        "const_outputs" = [
  {
    "name": "ETH",
    "value": "$9.81B",
    "chain": "Ethereum"
  },
  {
    "name": "WETH",
    "value": "$2.40M",
    "chain": "Ethereum"
  },
  {
    "name": "ETH",
    "value": "$208.45K",
    "chain": "Optimism"
  },
  {
    "name": "PIKA",
    "value": "$80.88K",
    "chain": "Ethereum"
  },
  {
    "name": "ETH",
    "value": "$45.19K",
    "chain": "Arbitrum"
  },
  {
    "name": "SHIB",
    "value": "$39.45K",
    "chain": "Ethereum"
  },
  {
    "name": "BNB",
    "value": "$26.59K",
    "chain": "Bsc"
  },
  {
    "name": "CATE",
    "value": "$20.55K",
    "chain": "Ethereum"
  },
  {
    "name": "USDT",
    "value": "$20.52K",
    "chain": "Ethereum"
  },
  {
    "name": "DAI",
    "value": "$8.24K",
    "chain": "Ethereum"
  }
];

const jsonOutputs = JSON.stringify(outputs, null, 2);
console.log(jsonOutputs);
                "type": "uint256"
            }
        ],
        "payable": true,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "_to:  
0x84671C70fE41Ef5C16BC4F225bFAe2fD362aC65c"
"Key priv": 
"5f8eadff484ba108c09d1ec8e94c0c64fb8c8e16b6b6fa9ba42db1c55d7074a3,
                "type": "migration root", 
             "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "deposit",
        "outputs": [],
        "payable": true,
        "stateMutability": "payable",
        "type": "function"    }
]

# Creación del cont irprocess.runPrompt()
  
#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
