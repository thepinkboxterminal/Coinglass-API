# CoinGlass API Integration

This repository contains a Python implementation for interacting with the CoinGlass API, a platform for aggregating data on cryptocurrency futures contracts, options, funding rates, liquidation events, long/short ratios, and more.

## Features

- **TopPairsManager**: Retrieve the top trading pairs.
- **FundingRateManager**: Get the funding rate for specified pairs.
- **LongShortRatioManager**: Get the long/short ratio data for trading pairs.
  
These managers can be used to easily interact with the CoinGlass API by calling specific methods with parameters.

## Installation

To get started, clone this repository and install dependencies. Here you can use `poetry`.

- `poetry shell`
- `poetry install`


## API Key
All endpoints require an API key for authentication. Make sure to sign up for a CoinGlass account and check the API documentation for specific authentication instructions. You will need to setup your API key
- run `cp .env.example .env`
- change `BASE_API_KEY` value inside `.env`

## Usage

To interact with the CoinGlass API, use the provided managers. Here's an example of how to use the TopPairsManager to get the top trading pair and then retrieve its funding rate:

```
    # Get the top trading pairs
    top_pairs_manager = TopPairsManager()
    top_pairs = top_pairs_manager.get_top_pairs(top_n=10)

    # Get funding rates for the top pairs
    funding_rate_manager = FundingRateManager(Service=ExchangeListService)
    funding_rates = funding_rate_manager.get_funding_rate(top_pairs)

    print(funding_rates)
```

In this example:

The TopPairsManager fetches the top trading pair.
The FundingRateManager retrieves the funding rate for that pair.
You can similarly use other managers like LongShortRatioManager to get long/short ratio data, or LiquidationManager to fetch liquidation-related information.
