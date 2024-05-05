const hre = require("hardhat")

const tokens = (n) => {
  return ethers.utils.parseUnits(n.toString(), 'ether')


}

async function main() {
    const Upload = await hre.ethers.getContractFactory("IPFS");
    const upload = await Upload.deploy();
    
    // Now, the contract address should be available
    console.log("Upload contract deployed with address:", upload.address);

    const [deployer] = await hre.ethers.getSigners();

    // Confirm deployer address
    console.log("Deployer address:", deployer.address);

    // Attempt to interact with the contract
    console.log("Calling upload_data function...");
    const trans = await upload.connect(deployer).addImage(1,"https://ipfs.io/ipfs/QmWosdKjs7yRtoUCJquWQugC4P2SZrnQc4FKb4A9gVHpct");
    await trans.wait();

    console.log(`Done uploading`);
    console.log(`Uploaded Data:- `)
    const uploadedData = await upload.getUserImages(deployer.address);

    console.log(uploadedData);
}

main().catch((error) => {
    console.error("Error:", error);
    process.exitCode = 1;
});