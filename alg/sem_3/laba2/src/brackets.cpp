#include "brackets.h"

bool bracketsFine(std::string line)
{
	std::vector<char> brackets(0);

	std::string str = line;

	bool flag = true;
	for (int i = 0; i < str.size(); ++i)
	{
		if (str[i] == '(' || str[i] == '[' || str[i] == '{')
		{
			brackets.push_back(str[i]);
		}
		else if (str[i] == ')' || str[i] == ']' || str[i] == '}')
		{
			if (brackets.size())
			{
				if (str[i] == ')')
				{
					if (brackets[brackets.size() - 1] != '(')
					{
						flag = false;
						throw "extra brackets";
						break;
					}
					else
					{
						brackets.pop_back();
					}
				}
				else
				{
					if (brackets[brackets.size() - 1] != str[i] - 2)
					{
						flag = false;
						throw "extra brackets";
						break;
					}
					else
					{
						brackets.pop_back();
					}
				}
			}
			else
			{
				flag = false;
				throw "extra brackets";
				break;
			}
		}
	}

	if (brackets.size() > 0)
	{
		flag = false;
		throw "extra brackets";
	}
	
	return flag;
}
