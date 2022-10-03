# ai-api-auditor-web

This heroku app shows the results of auditing an Artificial Intelligence (AI) API with an open source dataset. The scheduled job that runs the audit is open source [in the ai-auditor-cron repository](https://github.com/nlathia/ai-auditor-cron).

The initial version is set up to analyse the [Google Cloud Sentiment](https://cloud.google.com/natural-language/docs/analyzing-sentiment) service using the [Rotten Tomatoes](https://huggingface.co/datasets/rotten_tomatoes) dataset. The service could be extended to other APIs (for example, [Amazon's Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/how-sentiment.html) and datasets).



