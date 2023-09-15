#include <iostream>
#include <string>
#include <vector>
#include "brackets.h"

bool contains(char elem, std::vector<char>& line)
{
    for (int i = 0; i < line.size(); ++i)
    {
        if (line[i] == elem)
        {
            return true;
        }
    }
    return false;
}

int main()
{
    std::string line;
    std::cin >> line;
    std::string allOperands = "*/+-=()";
    
    try 
    {
        bracketsFine(line);
    }
    catch(const char* error)
    {
        std::cerr << error;
    }
    
    std::vector<char> operands(0);
    std::vector<std::string> rPolishNotation(0);

    std::string tempNum;
    
    bool flagEquals = false;
    for (int i = 0; i < line.length(); i++)
    {
        if (48 <= line[i] && line[i] <= 57)
        {
            tempNum += line[i];
        }
        else
        {
            try
            {
                if (allOperands.find(line[i]) == std::string::npos)
                {
                    throw "wrong expression";
                }
                if (tempNum.length() == 0 && line[i] != '(' && i == 0)
                {
                    throw "wrong operands";
                }
                if (tempNum.size() > 0 && (line[i] == '('))
                {
                    throw "missed *";
                }
            }
            catch (const char* error)
            {
                std::cerr << error << std::endl;
                exit(4);
            }
            if (tempNum.size() > 0)
            {
                rPolishNotation.push_back(tempNum);
                tempNum.clear();
            }
            int n = operands.size() - 1;
            if (line[i] == '*' || line[i] == '/')
            {
                if (operands.size() == 0 || operands[n] == '(' || operands[n] == '+' || operands[n] == '-')operands.push_back(line[i]);
                else
                {
                    while (operands[n] == '*' || operands[n] == '/')
                    {
                        std::string last = "";
                        last += operands[n];
                        rPolishNotation.push_back(last);
                        operands.pop_back();
                        n = operands.size() - 1;
                        if (operands.size() == 0)
                        {
                            break;
                        }
                    }
                    operands.push_back(line[i]);
                }
            }
            else if(line[i] == '+' || line[i] == '-')
            {
                if (operands.size() == 0)operands.push_back(line[i]);
                else
                {
                    while (operands[n] == '+' || operands[n] == '-' || operands[n] == '*' || operands[n] == '/')
                    {
                        std::string last = "";
                        last += operands[n];
                        rPolishNotation.push_back(last);
                        operands.pop_back();
                        n = operands.size() - 1;
                        if (operands.size() == 0)
                        {
                            break;
                        }
                    }
                    operands.push_back(line[i]);
                }
            }
            else if(line[i] == '(')
            {
                operands.push_back(line[i]);
            }
            else if (line[i] == ')')
            {
                while (operands[n] != '(')
                {
                    std::string last = "";
                    last += operands[n];
                    rPolishNotation.push_back(last);
                    operands.pop_back();
                    n = operands.size() - 1;
                    if (operands.size() == 0)
                    {
                        break;
                    }
                }
                operands.pop_back();
            }
            else if (line[i] == '=')
            {
                flagEquals = true;
                while (operands.size()!=0)
                {
                    std::string last = "";
                    last += operands[n];
                    rPolishNotation.push_back(last);
                    operands.pop_back();
                    n = operands.size() - 1;
                    if (operands.size() == 0)
                    {
                        break;
                    }
                }
            }
        }
    }
    std::vector<float> stackNumbers(0);
    if (flagEquals)
    {
        for (int i = 0; i < rPolishNotation.size(); ++i)
        {
            if (48 <= rPolishNotation[i][0] && 57 >= rPolishNotation[i][0]) stackNumbers.push_back(std::stof(rPolishNotation[i]));
            else
            {
                float a = stackNumbers[stackNumbers.size() - 1];
                float b = stackNumbers[stackNumbers.size() - 2];
                float res = 0;
                switch (rPolishNotation[i][0])
                {

                case '*':
                    res = a * b;
                    break;
                case '/':
                    if (a == 0)
                    {
                        std::cout << "division by 0";
                        exit(5);
                    }
                    else
                    {
                        res = b / a;
                        break;
                    }
                case '+':
                    res = a + b;
                    break;
                case '-':
                    res = b - a;
                    break;
                }
                stackNumbers.pop_back();
                stackNumbers.pop_back();
                stackNumbers.push_back(res);
            }
        }
        std::cout << stackNumbers[0];
    }
    else
    {
        std::cout << "no equals sign";
    }
    return 0;
}