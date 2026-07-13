from nlp_engine import NLPEngine
from tally_client import TallyClient

client = TallyClient()
engine = NLPEngine(client)

query = "List the parties to whom I need to make the payment this week"
print("Processing query...")
params = engine.parse_query(query)
print("Done")
