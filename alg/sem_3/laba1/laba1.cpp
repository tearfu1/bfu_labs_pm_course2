#include <iostream>
#include <vector>
#include <string>



int main()
{
	setlocale(LC_ALL, "Russian");
	std::vector<char> brackets(0);
	std::cout << "Введите строку" << std::endl;
	std::string str;
	std::cin >> str;
	
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
					if (brackets[brackets.size() - 1] != '(' )
					{
						flag = false;
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
				break;
			}
		}
	}

	if (brackets.size() > 0)
	{
		flag = false;
	}

	if (flag)
	{
		std::cout << "Строка существует";
	}
	else
	{
		std::cout << "Строка не существует";
	}
	return 0;
}