package inheritance;
public class Student extends Person
{
    private int studentNumber;

    public Student( )
    {
        super( );
        studentNumber = 0;//Indicating no number yet
    }

    public Student(String initialName, int initialStudentNumber)
    {
        super(initialName);
        studentNumber = initialStudentNumber;
    }

    public void reset(String newName, int newStudentNumber)
    {
        setName(newName);
        studentNumber = newStudentNumber;
    }

    public int getStudentNumber( )
    {
        return studentNumber;
    }

    public void setStudentNumber(int newStudentNumber)
    {
        studentNumber = newStudentNumber;
    }

    public void writeOutput( )
    {
        System.out.println("Name: " + getName( ));
        System.out.println("Student Number: " + studentNumber);
    }

    public boolean equals(Student otherStudent)
    {
        return this.hasSameName(otherStudent) &&
              (this.studentNumber == otherStudent.studentNumber);
    }


    public String toString( )
    {
        return "Name: " + getName( ) +
			   "\nStudent number: "  + studentNumber;
    }

 /* //For Optional Section
    public boolean equals(Object otherObject)
    {
        if (otherObject == null)
            return false;
        else if (!(otherObject instanceof Student))
            return false;
        else
        {
            Student otherStudent = (Student)otherObject;
            return (this.sameName(otherStudent)
                && (this.studentNumber ==
                                otherStudent.studentNumber));
        }
    }
*/

}
