from typing import Literal
from redbot.core import Config, commands
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import box, warning
from discord import Embed, TextChannel
from datetime import datetime

class Logger(commands.Cog):
    """_summary_

    Args:
        commands (_type_): _description_
    """
    
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self)
        
        self.config.register_global(
            channel=True,
            options=True,
            guild=True
        )
        
    
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
        c = await self.config.channel.set(channel)
        o = await self.config.options.set(option)
        
        logger_channel = await self.config.channel(c)
        logger_options = await self.config.options(o)
        
        if (option == 'guilds'):
            option_choice = 'Guild Join'
        else:
            if (option == "errors"):
                option_choice = 'Errors'
                
        
        e = Embed(title='Logger', description='Logger has been enabled', timestamp=datetime.utcnow())
        e.add_field(name='{}'.format(option_choice), value='{}'.format(logger_options), inline=True)        
        e.add_field(name='Logging Channel', value='{}'.format(logger_channel), inline=True)
        e.color('Blue')
        e.set_footer(text='Powered by Red-DiscordBot', icon_url='{}'.format(ctx.bot.getAvatarUrl()))
                
        await ctx.send(embed=e) 
        
        
        @Red.on_guild_join()
        async def on_guild_join(self, ctx):
            
            ch = await Config.channel(channel)
            logger_channel = await Config.channel(ch)
            
            e = Embed(title='Logger', description='{} has entered a new guild.'.format(ctx.bot.name), timestamp=datetime.utcnow())
            e.add_field(name='Guild Name', value='{}'.format(ctx.guild.name), inline=True),
            e.add_field(name='Guild ID', value='{}'.format(ctx.guild.id), inline=True)
            e.color('Blue')
            e.set_footer(text='Powered by Red-DiscordBot', icon_url='{}'.format(ctx.bot.getAvatarUrl()))
            await logger_channel.send(embed=e)