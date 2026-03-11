class EnvironmentalAgent:

    def analyze(self, message):

        message = message.lower()

        if "climate" in message or "carbon" in message:
            return "Environmental Agent Recommendation: Increase carbon reduction policies and invest in renewable energy."

        if "wildfire" in message or "forest" in message:
            return "Environmental Agent Recommendation: Increase forest management funding and wildfire prevention programs."

        if "water" in message:
            return "Environmental Agent Recommendation: Implement national water conservation initiatives."

        return None


class TechnologyAgent:

    def analyze(self, message):

        message = message.lower()

        if "ai" in message or "artificial intelligence" in message:
            return "Technology Agent Recommendation: Expand national AI research funding and develop ethical AI regulations."

        if "energy tech" in message or "renewable technology" in message:
            return "Technology Agent Recommendation: Increase funding for clean energy technology innovation."

        if "cybersecurity" in message:
            return "Technology Agent Recommendation: Strengthen national cybersecurity infrastructure."

        return None