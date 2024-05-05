require("@nomicfoundation/hardhat-toolbox");
require("dotenv").config()



/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.24",
  networks: {
    base: {
      url: "https://base-sepolia.g.alchemy.com/v2/ry0RpisMZsHyMTeS9y2SyEGqV-pMuxwO",
      accounts:[process.env.PRIVATE_KEY]

    },

    

  },

  etherscan:{

    apiKey: process.env.BASE_TOKEN

  }
};
