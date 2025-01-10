from typing import Any, Dict
from services.base import CoinglassAPIBase


class GlobalAccountRatioService(CoinglassAPIBase):
    def fetch_data(self, symbol: str, exchange: str = "Binance", interval: str = "1d") -> Dict[str, Any]:
        endpoint = "/futures/globalLongShortAccountRatio/history"
        params = {"symbol": symbol, "interval": interval, "exchange": exchange}
        return self._make_request(endpoint, params)

class TopAccountRatioHistoryService(CoinglassAPIBase):
    def fetch_data(self, symbol: str, exchange: str = "Binance", interval: str = "1d") -> Dict[str, Any]:
        endpoint = "/futures/topLongShortAccountRatio/history"
        params = {"symbol": symbol, "interval": interval, "exchange": exchange}
        return self._make_request(endpoint, params)

class TopPositionRatioHistoryService(CoinglassAPIBase):
    def fetch_data(self, symbol: str, exchange: str = "Binance", interval: str = "1d") -> Dict[str, Any]:
        endpoint = "/futures/topLongShortPositionRatio/history"
        params = {"symbol": symbol, "interval": interval, "exchange": exchange}
        return self._make_request(endpoint, params)

class AggregatedTakerBuySellHistoryService(CoinglassAPIBase):
    def fetch_data(self, symbol: str, exchange: str = "Binance", interval: str = "1d") -> Dict[str, Any]:
        endpoint = "/futures/aggregatedTakerBuySellVolumeRatio/history"
        params = {"symbol": symbol, "interval": interval, "exchange": exchange}
        return self._make_request(endpoint, params)
    
class AggregatedTakerBuySellVolumeHistoryService(CoinglassAPIBase):
    def fetch_data(self, symbol: str, exchange: str = "Binance", interval: str = "1d") -> Dict[str, Any]:
        endpoint = "/futures/aggregatedTakerBuySellVolume/history"
        params = {"symbol": symbol, "interval": interval, "exchange": exchange}
        return self._make_request(endpoint, params)

class TakerBuySellRatioHistoryService(CoinglassAPIBase):
    def fetch_data(self, symbol: str, exchange: str = "Binance", interval: str = "1d") -> Dict[str, Any]:
        endpoint = "/futures/takerBuySellVolume/history"
        params = {"symbol": symbol, "interval": interval, "exchange": exchange}
        return self._make_request(endpoint, params)

class ExchangeTakerBuySellRatioHistoryService(CoinglassAPIBase):
    def fetch_data(self, symbol: str, interval: str = "1d") -> Dict[str, Any]:
        endpoint = "/futures/takerBuySellVolume/exchange-list"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request(endpoint, params)
