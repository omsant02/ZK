// SPDX-License-Identifier: MIT
pragma solidity >=0.8.21;

import {Test} from "forge-std/Test.sol";
import {HonkVerifier} from "../src/Verifier.sol";

contract HashPreimageTest is Test {
    HonkVerifier internal verifier;

    function setUp() public {
        verifier = new HonkVerifier();
    }

    // Reads the public inputs file as a list of 32-byte words.
    // The file is just the words back to back, so we wrap them in the
    // standard ABI layout of a dynamic array (offset, length, words) and decode.
    function _loadPublicInputs() internal view returns (bytes32[] memory) {
        bytes memory raw = vm.readFileBinary("../target/public_inputs");
        return abi.decode(abi.encodePacked(uint256(32), uint256(raw.length / 32), raw), (bytes32[]));
    }

    // The real proof, made by `bb prove`, must be accepted.
    function test_validProofAccepted() public view {
        bytes memory proof = vm.readFileBinary("../target/proof");
        bytes32[] memory publicInputs = _loadPublicInputs();
        assertTrue(verifier.verify(proof, publicInputs));
    }

    // The same proof against a different statement must not pass.
    function test_wrongPublicInputRejected() public {
        bytes memory proof = vm.readFileBinary("../target/proof");
        bytes32[] memory publicInputs = _loadPublicInputs();
        publicInputs[0] = bytes32(uint256(publicInputs[0]) + 1);
        try verifier.verify(proof, publicInputs) returns (bool ok) {
            assertFalse(ok);
        } catch {
            // reverting also counts as rejecting
        }
    }
}