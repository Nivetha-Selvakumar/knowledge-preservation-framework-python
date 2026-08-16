class BaseAgent:

    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.status = "CREATED"

    async def perceive(self):
        pass

    async def reason(self):
        pass

    async def act(self):
        pass

    async def learn(self):
        pass

    async def adapt(self):
        pass

    async def execute(self):

        self.status = "RUNNING"

        await self.perceive()

        await self.reason()

        await self.act()

        await self.learn()

        await self.adapt()

        self.status = "ACTIVE"
