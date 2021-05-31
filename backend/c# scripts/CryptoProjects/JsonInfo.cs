using Newtonsoft.Json;

namespace CryptoProjects
{
    class JsonInfo
    {
            [JsonProperty("BTC")]
            public CryptoItem BTC { get; set; }
            [JsonProperty("ETH")]
            public CryptoItem ETH { get; set; }
            [JsonProperty("XRP")]
            public CryptoItem XRP { get; set; }
            [JsonProperty("BNB")]
            public CryptoItem BNB { get; set; }
            [JsonProperty("Doge")]
            public CryptoItem Doge { get; set; }
            [JsonProperty("LTC")]
            public CryptoItem LTC { get; set; }
            [JsonProperty("BCH")]
            public CryptoItem BCH { get; set; }
            [JsonProperty("EOS")]
            public CryptoItem EOS { get; set; }
            [JsonProperty("XLM")]
            public CryptoItem XLM { get; set; }
            [JsonProperty("TRX")]
            public CryptoItem TRX { get; set; }
            [JsonProperty("DASH")]
            public CryptoItem DASH { get; set; }
            [JsonProperty("LINK")]
            public CryptoItem LINK { get; set; }
  
    }

}
