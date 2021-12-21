
class OperatorStack:
    """class which contains the different operations
    """
    @staticmethod
    def addition_stack(stack):
        """function addition

        Args:
            stack ([dict]): [dict of stack]

        Returns:
            [dict]: [dif of stack]
        """
        print(stack)
        stack[-2] = stack[-1]+stack[-2]
        stack.remove(stack[-1])
        return stack

    @staticmethod
    def substraction_stack(stack):
        """function substraction

        Args:
            stack ([dict]): [dict of stack]

        Returns:
            [dict]: [dif of stack]
        """
        stack[-2] = stack[-1]-stack[-2]
        stack.remove(stack[-1])
        return stack

    @staticmethod
    def multiplication_stack(stack):
        """function multiplication

        Args:
            stack ([dict]): [dict of stack]

        Returns:
            [dict]: [dif of stack]
        """
        stack[-2] = stack[-1]*stack[-2]
        stack.remove(stack[-1])
        return stack

    @staticmethod
    def division_stack(stack):
        """function division

        Args:
            stack ([dict]): [dict of stack]

        Returns:
            [dict]: [dif of stack]
        """
        stack[-2] = stack[-1]/stack[-2]
        stack.remove(stack[-1])
        return stack
