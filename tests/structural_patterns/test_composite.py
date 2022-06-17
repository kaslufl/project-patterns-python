from project_patterns import Composite, Leaf


def test_composite():
    main = Composite('Main Menu')
    option = Composite('Sub Menu')
    option2 = Composite('Sub Menu2')

    sub_option = Leaf('Option1')
    sub_option2 = Leaf('Option2')
    sub_option3 = Leaf('Option3')
    sub_option4 = Leaf('Option4')

    option.add(sub_option)
    option.add(sub_option2)

    option2.add(sub_option3)
    option2.add(sub_option4)

    main.add(option)
    main.add(option2)
    print(main.operation())
    assert main.operation() == 'Main Menu\n\tSub Menu\n\t\tOption1\n\t\tOption2\n\tSub Menu2\n\t\tOption3\n\t\tOption4'