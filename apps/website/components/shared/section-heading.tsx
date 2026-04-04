interface SectionHeadingProps {
  number: string
  title: string
}

export function SectionHeading({ number, title }: SectionHeadingProps) {
  return (
    <div className="mb-12 md:mb-16 max-w-[720px] mx-auto">
      <span className="section-label">
        {number} &mdash; {title}
      </span>
    </div>
  )
}
