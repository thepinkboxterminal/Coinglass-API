from managers.base import FundingRateManager, TopPairsManager
from services.funding_rates import ExchangeListService


def main():
    top_pairs_manager = TopPairsManager()
    top_pairs = top_pairs_manager.get_top_pairs(top_n=1)

    funding_rate_manager = FundingRateManager(Service=ExchangeListService)
    funding_rates = funding_rate_manager.get_funding_rate(top_pairs)
    print(funding_rates)


if __name__ == "__main__":
    main()
