using Newtonsoft.Json;

namespace CryptoParseDLL
{
    class CryptoItem
    {
        public string Date { get; set; }
        [JsonProperty("USD")]
        public string USD { get; set; }
        [JsonProperty("EUR")]
        public string EUR { get; set; }

    }
}
