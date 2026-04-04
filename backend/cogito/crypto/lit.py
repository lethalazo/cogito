"""Lit Protocol integration - decentralized access control and key management.

Lit Protocol provides decentralized encryption and access control without a centralized
key custodian. It uses a network of nodes to enforce access conditions (e.g., "only the
wallet owner can decrypt this data") without any single node having the full key.

Use cases in Cogito:
- Encrypting user data with access conditions (only wallet owner can decrypt)
- Sharing encrypted data with specific wallets (future: shared cognition between users)
- Decentralized key management - no centralized key server to trust or compromise
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AccessControlCondition:
    """A Lit Protocol access control condition.

    Defines who can decrypt data. Conditions can be combined with boolean logic.

    Attributes:
        contract_address: The contract to check (empty string for native balance checks).
        chain: The blockchain to check (e.g., "ethereum").
        method: The method to call (e.g., "" for balance, "balanceOf" for ERC-20).
        parameters: Method parameters (e.g., [":userAddress"] for the requesting user).
        return_value_test: Comparison test for the return value.
    """

    contract_address: str = ""
    chain: str = "ethereum"
    method: str = ""
    parameters: list[str] = field(default_factory=list)
    return_value_test: dict[str, Any] = field(default_factory=dict)


class LitClient:
    """Client for interacting with the Lit Protocol network.

    Handles connection to Lit nodes, encrypting data with access control conditions,
    and decrypting data when conditions are met.
    """

    def __init__(self, network: str = "cayenne") -> None:
        self.network = network

    async def connect(self) -> None:
        """Connect to the Lit Protocol network.

        Initializes the Lit node client and establishes connections
        to the decentralized key management network.
        """
        raise NotImplementedError

    async def encrypt_with_access_control(
        self,
        data: bytes,
        access_control_conditions: list[AccessControlCondition],
    ) -> dict[str, Any]:
        """Encrypt data with Lit Protocol access control.

        The data can only be decrypted by wallets meeting the access control conditions.

        Args:
            data: The plaintext data to encrypt.
            access_control_conditions: Conditions that must be met to decrypt.

        Returns:
            Dict with "ciphertext" and "data_to_encrypt_hash" for later decryption.
        """
        raise NotImplementedError

    async def decrypt_with_access_control(
        self,
        ciphertext: str,
        data_to_encrypt_hash: str,
        access_control_conditions: list[AccessControlCondition],
        auth_sig: dict[str, Any],
    ) -> bytes:
        """Decrypt data using Lit Protocol.

        The caller must provide an auth signature proving they meet the access conditions.

        Args:
            ciphertext: The encrypted data from encrypt_with_access_control.
            data_to_encrypt_hash: The hash from encrypt_with_access_control.
            access_control_conditions: The same conditions used during encryption.
            auth_sig: The caller's authentication signature.

        Returns:
            The decrypted plaintext bytes.
        """
        raise NotImplementedError

    @staticmethod
    def wallet_owner_condition(wallet_address: str) -> AccessControlCondition:
        """Create an access control condition for wallet ownership.

        Only the owner of the specified wallet can decrypt the data.

        Args:
            wallet_address: The Ethereum wallet address (checksummed).

        Returns:
            An AccessControlCondition that checks wallet ownership.
        """
        raise NotImplementedError
