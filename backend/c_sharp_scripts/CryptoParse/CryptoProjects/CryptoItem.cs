using Newtonsoft.Json;

namespace CryptoProjects
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
