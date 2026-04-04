interface LogoProps {
  size?: number
  className?: string
}

export function Logo({ size = 40, className }: LogoProps) {
  const width = size * 0.75
  const height = size

  return (
    <svg
      width={width}
      height={height}
      viewBox="0 0 60 80"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      className={className}
      aria-hidden="true"
    >
      <defs>
        <radialGradient id="cogito-glow-top" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stopColor="#D4635E" stopOpacity="0.5" />
          <stop offset="100%" stopColor="#D4635E" stopOpacity="0" />
        </radialGradient>
        <radialGradient id="cogito-glow-bottom" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stopColor="#D4635E" stopOpacity="0.5" />
          <stop offset="100%" stopColor="#D4635E" stopOpacity="0" />
        </radialGradient>
      </defs>

      {/* C curve: open on the right, connecting top and bottom particles */}
      <path
        d="M 45 10 C 10 10, 4 28, 4 40 C 4 52, 10 70, 45 70"
        stroke="#D4635E"
        strokeWidth="1.8"
        strokeOpacity="0.5"
        strokeLinecap="round"
        fill="none"
      />

      {/* Top particle - glow */}
      <circle cx="45" cy="10" r="9" fill="url(#cogito-glow-top)" />
      {/* Top particle - core */}
      <circle cx="45" cy="10" r="3.5" fill="#D4635E" />

      {/* Bottom particle - glow */}
      <circle cx="45" cy="70" r="9" fill="url(#cogito-glow-bottom)" />
      {/* Bottom particle - core */}
      <circle cx="45" cy="70" r="3.5" fill="#D4635E" />
    </svg>
  )
}
