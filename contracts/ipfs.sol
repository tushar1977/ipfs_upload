// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.9;

contract IPFS {
    struct Image {
        uint256 id;
        string image;
    }

    mapping(address => Image[]) public userImages;

    function addImage(uint256 _id, string memory _image) public {
        Image memory newImage = Image(_id, _image);
        userImages[msg.sender].push(newImage);
    }

    function getUserImages(
        address user
    ) public view returns (uint256[] memory, string[] memory) {
        Image[] memory images = userImages[user];
        uint256[] memory ids = new uint256[](images.length);
        string[] memory imageUrls = new string[](images.length);

        for (uint256 i = 0; i < images.length; i++) {
            ids[i] = images[i].id;
            imageUrls[i] = images[i].image;
        }

        return (ids, imageUrls);
    }
}
