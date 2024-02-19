from typing import Literal
from redbot.core import Config, commands
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import box, warning
from discord import Embed, TextChannel

class Logger(commands.Cog):
    """_summary_

    Args:
        commands (_type_): _description_
    """
    
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self)
        
        logger_config = {
            # ...   
        }
        
        self.config.register_global(**logger_config)
        
    
    @commands.group()
    @commands.is_owner()
    async def logger(self, ctx):
        """_summary_

        Args:
            ctx (_type_): _description_
        """
        pass
    
    @logger.command()
    async def channel(self, ctx, option: Literal["guilds", "errors"], channel: TextChannel):
        """_summary_

        Args:
            ctx (_type_): _description_
            option (Literal[&quot;guilds&quot;, &quot;errors&quot;]): _description_
            channel (TextChannel): _description_
        """
        ch = await self.config.set(channel)
        opt = await self.config.set(option)
        
        logger_channel = await Config.channel(ch)
        logger_options = await Config.option(opt)
        
        if (option == 'guilds'):
            option_choice = 'Guild Join'
        else:
            if (option == "errors"):
                option_choice = 'Errors'
                
        
        e = Embed(title='Logger', description='Logger has been enabled')
        e.add_field(name='{}'.format(option_choice), value='{}'.format(logger_options), inline=True)        
        e.add_field(name='Logging Channel', value='{}'.format(logger_channel), inline=True)
        e.color('Blue')
                
        await ctx.send(embed=e) 