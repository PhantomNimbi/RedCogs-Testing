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
            channel=True
        )
        
    
    @commands.group()
    @commands.is_owner()
    async def logger(self, ctx):
        """_summary_

        Args:
            ctx (_type_): _description_
        """
        pass
    
    @logger.command(name='channel')
    async def set_channel(self, ctx, channel: TextChannel):
        """_summary_

        Args:
            ctx (_type_): _description_
            option (Literal[&quot;guilds&quot;, &quot;errors&quot;]): _description_
            channel (TextChannel): _description_
        """
        await self.config.channel.set(channel)
        
        await ctx.send('Successfully enabled logger') 
        
        
        @commands.Cog.listener()
        async def on_guild_join(self, ctx, guild):
            """_summary_

            Args:
                ctx (_type_): _description_
                guild (_type_): _description_
            """
            
            if (self.config.channel == None):                
                return
            else:
                logger_channel = await ctx.get_channel(self.config.channel)
            
                e = Embed(title='Logger', description='{} has entered a new guild.'.format(ctx.bot.name), timestamp=datetime.utcnow())
                e.add_field(name='Guild Name', value='{}'.format(box[guild.name]), inline=True),
                e.add_field(name='Guild ID', value='{}'.format(box[guild.id]), inline=True)
                e.color('Blue')
                e.set_footer(text='Powered by Red-DiscordBot', icon_url='{}'.format(ctx.bot.getAvatarUrl()))
                await logger_channel.send(embed=e)
            
            
        @commands.Cog.listener()
        async def on_error(self, ctx, guild, error):
            """_summary_

            Args:
                ctx (_type_): _description_
                guild (_type_): _description_
                error (_type_): _description_
            """
            
            if (self.config.channel == None):                
                return
            else:
                logger_channel = await ctx.get_channel(self.config.channel)
            
            
                e = Embed(title='Logger', description='{} has encountered an error!'.format(ctx.bot.name), timestamp=datetime.utcnow())
                e.add_field(name='Guild Name', value='{}'.format(box[guild.name]), inline=True),
                e.add_field(name='Guild ID', value='{}'.format(box[guild.id]), inline=True)
                e.add_field(name='\u200b', value='\u200b')
                e.add_field(name='Error Stack', value='{}'.format(warning[error.stack]), inline=False)
                e.color('Blue')
                e.set_footer(text='Powered by Red-DiscordBot', icon_url='{}'.format(ctx.bot.getAvatarUrl()))
                await logger_channel.send(embed=e)