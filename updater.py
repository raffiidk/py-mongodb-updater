
    if message.content.startswith('$log'):
      user = message.author
      
      
      Embed = discord.Embed(title="**Log Data Required**",description="Client,Client ID,Date,Price,Platform fees,Converter fees,Converter,Payment In,Payment Out, Transcript,Security Fee. Separate with comma.", color=0xe23434)    
      await channel.send(embed=Embed)
      msgstr = str(message.content)
      print(msgstr)
      
      while True:
        msg = await client2.wait_for('message')
        if msg.author == message.author:
          content = msg.content
          string = str(content)
          split = string.split(",")
          log_data = split
          insertRow = log_data
          user = str(user)
          try:
            insertRow[3] = float(insertRow[3])
            print("row3")
            insertRow[4] = float(insertRow[4])
            #print("row4")
            insertRow[5] = float(insertRow[5])
            print("done int conv")
          except ValueError:
            await channel.send("`Error converting to int, most likely data incomplete.`")
            Embed = discord.Embed(title="**Log Data Required**",description="Client,Client ID,Date,Price,Platform fees,Converter fees,Converter,Payment In,Payment Out, Transcript,Security Fee. Separate with comma.", color=0xe23434)    
            await channel.send(embed=Embed)
            continue
          print(len(insertRow))
          if len(insertRow) < 10 and len(insertRow) > 7:
            print(len(insertRow))
            await channel.send("`Experimental feature triggered due to incomplete list...`")
            print("experimental")
            for i in range(11):
              if len(insertRow) == i:
                print(i)
                num = 11 - i
                print("Num, {}".format(num))
            if num > 0:
              for i in range(num):
                print("No data")
                insertRow.append("No data")
                continue
          if len(insertRow) < 8:
            await channel.send("`Incomplete data list.`")
            Embed = discord.Embed(title="**Log Data Required**",description="Client,Client ID,Date,Price,Platform fees,Converter fees,Converter,Payment In,Payment Out, Transcript,Security Fee. Separate with comma.", color=0xe23434)
            await channel.send(embed=Embed)
            continue
          datainsert = []
          counter = len(insertRow)
          for i in range(0,counter):  
            datainsert.append(insertRow[i])
          user = message.author
          user2 = user.id
          user4 = str(user2)
          user3 = str(user)
          channel2 = message.channel
          channel3 = str(channel2)
          time2 = date.today()
          time3 = str(time2)
          datainsert.append(user3)
          datainsert.append(user4)
          datainsert.append(time3)
          datainsert.append(channel3)     
          print(datainsert,"f")
          datasheet.insert_row(datainsert)
                 
          mongodata = {
            'client': datainsert[0],
            'discordId': datainsert[1],
            'date': datainsert[2],
            'price': datainsert[3],
            'platformFees': datainsert[4],
            'converterFees': datainsert[5],
            'converter': datainsert[6],
            'paymentIn': datainsert[7],
            'paymentOut': datainsert[8],
            'securityFees': datainsert[9],
            'transcript': datainsert[10],
            'logger': datainsert[11],
            'loggerId': datainsert[12],
            'logDate': datainsert[13],
            'logChannel': datainsert[14]
          }
          print("JSON Written")
          result = db.newbase.insert_one(mongodata)
          print(result,"r")
          print("Logged Object ID: {}".format(result.inserted_id))
          await channel.send("`Logged Object ID: {}`".format(result.inserted_id))
          
          Embed = discord.Embed(title="**Data Logged**",description="Logged by {}".format(user), color=0xe23434)    
          await channel.send(embed=Embed)
          msgdump = client2.get_channel(<ID>)
          botdump = client2.get_channel(<ID>)
          
          users = []
          for member in message.channel.members:
            print(member)
            for role in member.roles:
                print(role)
                if role.id == 767804261298864250:
                  print(id)
                  print("has role")                    
                  mid = member.id
                  users.append(mid)
                  
          
          await msgdump.send("```Logged by {}. Logged data: \n {}```".format(user,datainsert))
          await botdump.send("```Logged by {}. DB Object: {}. Users in ticket: {}```".format(user,result.inserted_id,users))
          
          catid = channel.category_id
          if catid == <ID>:
            await channel.send("Deleting channel, ticket has been logged")
            await channel.delete()
          break
    
