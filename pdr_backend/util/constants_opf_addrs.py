from enforce_typing import enforce_types

from pdr_backend.util.constants import (
    SAPPHIRE_TESTNET_CHAINID,
    SAPPHIRE_MAINNET_CHAINID,
)


@enforce_types
def get_opf_addresses(chain_id: int):
    if chain_id == SAPPHIRE_TESTNET_CHAINID:
        return {
            "predictoor1": "0xE02A421dFc549336d47eFEE85699Bd0A3Da7D6FF",
            "predictoor2": "0x00C4C993e7B0976d63E7c92D874346C3D0A05C1e",
            "predictoor3": "0x005C414442a892077BD2c1d62B1dE2Fc127E5b9B",
            "trueval": "0x005FD44e007866508f62b04ce9f43dd1d36D0c0c",
            "websocket": "0x008d4866C4071AC9d74D6359604762C7B581D390",
            "dfbuyer": "0xeA24C440eC55917fFa030C324535fc49B42c2fD7",
        }

    if chain_id == SAPPHIRE_MAINNET_CHAINID:
        return {
            "predictoor1": "0x35Afee1168D1e1053298F368488F4eE95E891a6e",
            "predictoor2": "0x1628BeA0Fb859D56Cd2388054c0bA395827e4374",
            "predictoor3": "0x3f0825d0c0bbfbb86cd13C7E6c9dC778E3Bb44ec",
            "predictoor4": "0x20704E4297B1b014d9dB3972cc63d185C6C00615",
            "predictoor5": "0xf38426BF6c117e7C5A6e484Ed0C8b86d4Ae7Ff78",
            "predictoor6": "0xFe4A9C5F3A4EA5B1BfC089713ed5fce4bB276683",
            "predictoor7": "0x078F083525Ad1C0d75Bc7e329EE6656bb7C81b12",
            "predictoor8": "0x4A15CC5C20c5C5F71A9EA6376356f72b2A760f12",
            "predictoor9": "0xD2a24CB4ff2584bAD80FF5F109034a891c3d88dD",
            "predictoor10": "0x8a64CF23B5BB16Fd7444B47f94673B90Cc0F75cE",
            "predictoor11": "0xD15749B83Be987fEAFa1D310eCc642E0e24CadBA",
            "predictoor12": "0xAAbDBaB266b31d6C263b110bA9BE4930e63ce817",
            "predictoor13": "0xB6431778C00F44c179D8D53f0E3d13334C051bd3",
            "predictoor14": "0x2c2C599EC040F47C518fa96D08A92c5df5f50951",
            "predictoor15": "0x5C72F76F7dae16dD34Cb6183b73F4791aa4B3BC4",
            "predictoor16": "0x19C0A543664F819C7F9fb6475CE5b90Bfb112d26",
            "predictoor17": "0x8cC3E2649777d59809C8d3E2Dd6E90FDAbBed502",
            "predictoor18": "0xF5F2a495E0bcB50bF6821a857c5d4a694F5C19b4",
            "predictoor19": "0x4f17B06177D37E24158fec982D48563bCEF97Fe6",
            "predictoor20": "0x784b52987A894d74E37d494F91eD03a5Ab37aB36",
            "predictoor21": "0x74c52ce6c26780B78140D183596F6a8Dfa135BE3",
            "predictoor22": "0xD5968dF47a9affF032B978272FFA0488f501cb48",
            "predictoor23": "0xB9b7DD5D22A9422da0d99bd76811c56B42041f7b",
            "predictoor24": "0x558072F52D9214C82504156f6699Acc803777dD9",
            "predictoor25": "0xB85fABEf56a2C909228E04B9E8b544C7704AFdF4",
            "predictoor26": "0x2B7dD01eC0Fa9Bd721A51D443714183cB47C1f89",
            "predictoor27": "0x17aC47B71Ac41704102450eA021b68cF63D245e5",
            "predictoor28": "0x61c2467aF26E833900e2Cbf36AfC2052C74523F5",
            "predictoor29": "0x192a209a02a62a9ac7871f4b1522bcB95DE46ecc",
            "predictoor30": "0x01e5c6628D4444623325D45D14009FE16ba7954b",
            "predictoor31": "0x821843bE901ae924f4E89eABF5CC6d02c5dcA70D",
            "predictoor32": "0x9c69d3fADC2CE6B4DfAc3506be5858Bb3E7cDA6e",
            "predictoor33": "0x557c689d7c337b1e1Df96B372bC37D4049AE047B",
            "predictoor34": "0x55e71ED6E08C227795B93313d692790D7EB096b3",
            "predictoor35": "0x59989A8fBff8be3d1deAFFF2b46B66B63ACB797e",
            "predictoor36": "0x3F4d0673058762075A31F6Df41782A942C24fC4B",
            "predictoor37": "0x601e4a6c892EAAF4f395bF3149D05Af3e26CCB3f",
            "predictoor38": "0x1ae9137c0CEC302d114ab5F8E7388Bc9D8a08100",
            "predictoor39": "0xe007bdFD1B8ab282f082CdE2046437ebe0D394fD",
            "predictoor40": "0x794Bf246d2bB9B8422accD83Af49934582c2f49A",
            "trueval": "0x886A892670A7afc719Dcf36eF92c798203F74B67",
            "websocket": "0x6Cc4Fe9Ba145AbBc43227b3D4860FA31AFD225CB",
            "dfbuyer": "0x2433e002Ed10B5D6a3d8d1e0C5D2083BE9E37f1D",
        }

    raise ValueError(chain_id)