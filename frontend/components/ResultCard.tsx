export default function ResultCard({ data }: any) {
    return (
      <div className="mt-6 bg-slate-900 rounded p-4">
        <p><b>Name:</b> {data.details.name}</p>
        <p><b>Hall Ticket:</b> {data.details.rollNo}</p>
        <p><b>College:</b> {data.details.college}</p>
  
        {data.results.map((exam: any, i: number) => (
          <div key={i} className="mt-4">
            <h3 className="text-sky-400 font-bold">
              Exam Code: {exam.examCode}
            </h3>
  
            {exam.subjects.map((sub: any, j: number) => (
              <div
                key={j}
                className="flex justify-between text-sm border-b border-slate-700 py-1"
              >
                <span>{sub.subjectName}</span>
                <span className="font-bold">{sub.grade}</span>
              </div>
            ))}
          </div>
        ))}
      </div>
    );
  }
  