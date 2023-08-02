import time
import os
import math
import random


from pdr_backend.dfbuyer.utils.subgraph import get_consume_so_far
from pdr_backend.utils.subgraph import get_all_interesting_prediction_contracts
from pdr_backend.utils.contract import PredictorContract, Web3Config


# TODO - check for all envs
assert os.environ.get("RPC_URL", None), "You must set RPC_URL environment variable"
assert os.environ.get(
    "SUBGRAPH_URL", None
), "You must set SUBGRAPH_URL environment variable"

avergage_time_between_blocks = 0
last_block_time = 0
WEEK = 7 * 86400

web3_config = Web3Config(os.environ.get("RPC_URL"), os.environ.get("PRIVATE_KEY"))
owner = web3_config.owner


def numbers_with_sum(n, k):
    print(f"numbers_with_sum ({n},{k})")
    if n < 1:
        return []
    if n == 1:
        return [k]
    num = random.randint(1, k)
    return [num] + numbers_with_sum(n - 1, k - num)


""" Get all intresting topics that we can predict.  Like ETH-USDT, BTC-USDT """
topics = []
predictoor_contracts = []


def process_block(block, avergage_time_between_blocks):
    global topics
    """ Process each contract and see if we need to submit """
    if not topics:
        topics = get_all_interesting_prediction_contracts(
            os.environ.get("SUBGRAPH_URL"),
            os.environ.get("PAIR_FILTER", None),
            os.environ.get("TIMEFRAME_FILTER", None),
            os.environ.get("SOURCE_FILTER", None),
            os.environ.get("OWNER_ADDRS", None),
        )
    if len(topics) < 1:
        return
    # how many estimated blocks till end of week?
    estimated_week_start = (math.floor(block["timestamp"] / WEEK)) * WEEK
    print(f"estimated_week_start:{estimated_week_start}")
    # get consume so far
    consume_so_far = get_consume_so_far(topics, estimated_week_start, owner)
    print(f"consume_so_far:{consume_so_far}")
    consume_left = float(os.getenv("WEEKLY_SPEND_LIMIT", 0)) - consume_so_far
    print(f"consume_left:{consume_left}")
    if consume_left <= 0:
        return
    estimated_week_end = estimated_week_start + WEEK
    print(f"estimated_week_end:{estimated_week_end}")
    estimated_blocks_left = (
        estimated_week_end - block["timestamp"]
    ) / avergage_time_between_blocks
    print(f"estimated_blocks_left:{estimated_blocks_left}")
    consume_target = random.uniform(0, consume_left / estimated_blocks_left * 100)
    print(f"consume_target:{consume_target}")
    # do random allocation
    buy_percentage_per_topic = numbers_with_sum(len(topics), 100)
    print(f"buy_percentage_per_topic:{buy_percentage_per_topic}")
    print(f"Got new block: {block['number']} with {len(topics)} topics")
    cnt = 0
    for address in topics:
        print(f"Percentage:{buy_percentage_per_topic[cnt]}")
        max_to_spend = consume_target * (buy_percentage_per_topic[cnt] / 100)
        predictor_contract = PredictorContract(web3_config, address)
        price = predictor_contract.get_price() / 10**18
        txs = predictor_contract.buy_many(
            int(max_to_spend / price), int(block["gasLimit"] * 0.99)
        )
        print(txs)
        cnt = cnt + 1


def log_loop(blockno):
    global avergage_time_between_blocks, last_block_time
    block = web3_config.w3.eth.get_block(blockno, full_transactions=False)
    if block:
        if last_block_time > 0:
            avergage_time_between_blocks = (
                avergage_time_between_blocks + (block["timestamp"] - last_block_time)
            ) / 2
        last_block_time = block["timestamp"]
    if avergage_time_between_blocks > 0:
        process_block(block, avergage_time_between_blocks)


def main():
    print("Starting main loop...")
    lastblock = 0
    while True:
        block = web3_config.w3.eth.block_number
        if block > lastblock:
            lastblock = block
            log_loop(block)
        else:
            time.sleep(1)


if __name__ == "__main__":
    main()
